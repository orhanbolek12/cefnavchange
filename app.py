"""
CEF NAV Tracker - Real-Time Edition
Flask backend that scrapes Morningstar for holdings and serves the dashboard.
Finnhub WebSocket connects directly from the browser for real-time prices.
"""
from flask import Flask, jsonify, send_from_directory
import requests
import json
import os
import re
import time
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')

# Cache for holdings data (so we don't hammer Morningstar)
holdings_cache = {}
CACHE_DURATION = 3600  # 1 hour cache

# CEF tickers and their Morningstar security IDs
# Format: { "CEF_TICKER": { "secId": "MORNINGSTAR_SEC_ID", "exchange": "XNYS" } }
CEF_REGISTRY = {
    "BME":  {"secId": "0P00005VHS", "exchange": "XNYS"},
    "BMEZ": {"secId": "0P0001HIIX", "exchange": "XNYS"},
    "GRX":  {"secId": "0P00005VHT", "exchange": "XNYS"},
    "HQH":  {"secId": "0P00005VHH", "exchange": "XNYS"},
    "HQL":  {"secId": "0P00005VHI", "exchange": "XNYS"},
    "THW":  {"secId": "0P0000YXBH", "exchange": "XNYS"},
    "THQ":  {"secId": "0P00005VHG", "exchange": "XNYS"},
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.morningstar.com",
    "Referer": "https://www.morningstar.com/",
}


def fetch_morningstar_holdings(cef_ticker):
    """Fetch holdings for a CEF from Morningstar's internal API."""
    info = CEF_REGISTRY.get(cef_ticker)
    if not info:
        return None

    sec_id = info["secId"]

    # Try the sal-service API endpoint (used by Morningstar's frontend)
    urls_to_try = [
        f"https://api-global.morningstar.com/sal-service/v1/fund/portfolio/holding/v2/{sec_id}/data",
        f"https://api-global.morningstar.com/sal-service/v1/fund/portfolio/v2/{sec_id}/data",
    ]

    params = {
        "premiumNum": "10000",
        "freeNum": "10000",
        "langcult": "en-US",
        "sal-siteid": "MCYJzSTSaJ0=",
        "sal-contentType": "e7FDDltr6TH+w9sRP5JWTg==",
    }

    for url in urls_to_try:
        try:
            resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                return parse_morningstar_response(data, cef_ticker)
        except Exception as e:
            print(f"[{cef_ticker}] API attempt failed for {url}: {e}")
            continue

    # Fallback: try scraping the HTML page
    try:
        return scrape_morningstar_page(cef_ticker, sec_id)
    except Exception as e:
        print(f"[{cef_ticker}] HTML scrape also failed: {e}")

    return None


def parse_morningstar_response(data, cef_ticker):
    """Parse Morningstar API JSON response into holdings list."""
    holdings = []
    portfolio_date = None

    # Try different JSON structures
    holding_lists = []
    if isinstance(data, dict):
        # Structure 1: { "equityHoldingPage": { "holdingList": [...] } }
        eq = data.get("equityHoldingPage", {})
        if eq:
            holding_lists = eq.get("holdingList", [])
            portfolio_date = data.get("portfolioDate") or eq.get("portfolioDate")

        # Structure 2: { "holdingList": [...] }
        if not holding_lists:
            holding_lists = data.get("holdingList", [])
            portfolio_date = data.get("portfolioDate")

        # Structure 3: { "allHolding": [...] }
        if not holding_lists:
            holding_lists = data.get("allHolding", [])
            portfolio_date = data.get("portfolioDate")

    for h in holding_lists:
        symbol = h.get("ticker") or h.get("symbol") or h.get("holdingTicker", "")
        weight = h.get("weighting") or h.get("percentAssets") or h.get("portfolioPercent") or h.get("weight", 0)
        name = h.get("securityName") or h.get("holdingName") or h.get("name", "")

        if symbol and weight:
            try:
                weight_val = float(weight)
                if weight_val > 0:
                    holdings.append({
                        "symbol": symbol.strip(),
                        "weight": round(weight_val, 2),
                        "name": name
                    })
            except (ValueError, TypeError):
                continue

    return {
        "ticker": cef_ticker,
        "holdings": holdings,
        "portfolioDate": portfolio_date,
        "source": "morningstar_api",
        "fetchedAt": datetime.now().isoformat()
    }


def scrape_morningstar_page(cef_ticker, sec_id):
    """Fallback: scrape the Morningstar portfolio page HTML."""
    url = f"https://www.morningstar.com/cefs/xnys/{cef_ticker.lower()}/portfolio"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return None

        # Try to find embedded JSON data in the HTML
        text = resp.text

        # Look for __NEXT_DATA__ or similar JSON blobs
        patterns = [
            r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',
            r'window\.__INITIAL_STATE__\s*=\s*({.*?});',
            r'"holdingList"\s*:\s*(\[.*?\])',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group(1))
                    result = parse_morningstar_response(data, cef_ticker)
                    if result and result["holdings"]:
                        return result
                except json.JSONDecodeError:
                    continue

    except Exception as e:
        print(f"[{cef_ticker}] Scrape error: {e}")

    return None


def get_fallback_holdings():
    """Load holdings from local all_holdings.json as ultimate fallback."""
    # Check if the old cefholdings project has data
    fallback_path = os.path.join(os.path.dirname(__file__), "holdings_fallback.json")
    if os.path.exists(fallback_path):
        with open(fallback_path, 'r') as f:
            return json.load(f)

    # Try the old project path
    old_path = os.path.expanduser("~/Desktop/cefholdings/all_holdings.json")
    if os.path.exists(old_path):
        with open(old_path, 'r') as f:
            raw = json.load(f)
            result = {}
            for cef, stocks in raw.items():
                result[cef] = {
                    "ticker": cef,
                    "holdings": stocks,
                    "portfolioDate": None,
                    "source": "local_fallback",
                    "fetchedAt": datetime.now().isoformat()
                }
            return result

    return {}


@app.route('/')
def index():
    """Serve the main dashboard."""
    return send_from_directory('.', 'index.html')


@app.route('/api/holdings')
def get_all_holdings():
    """Return holdings for all CEFs. Uses cache to avoid hammering Morningstar."""
    global holdings_cache
    now = time.time()

    # Check if cache is still valid
    if holdings_cache and (now - holdings_cache.get("_timestamp", 0)) < CACHE_DURATION:
        return jsonify(holdings_cache)

    result = {"_timestamp": now, "cefs": {}}
    fallback_data = get_fallback_holdings()

    for cef_ticker in CEF_REGISTRY:
        print(f"Fetching holdings for {cef_ticker}...")
        data = fetch_morningstar_holdings(cef_ticker)

        if data and data["holdings"]:
            result["cefs"][cef_ticker] = data
            print(f"  [OK] {cef_ticker}: {len(data['holdings'])} holdings from Morningstar")
        elif cef_ticker in fallback_data:
            # Use fallback
            fb = fallback_data[cef_ticker]
            if isinstance(fb, dict):
                result["cefs"][cef_ticker] = fb
            else:
                result["cefs"][cef_ticker] = {
                    "ticker": cef_ticker,
                    "holdings": fb,
                    "portfolioDate": None,
                    "source": "local_fallback",
                    "fetchedAt": datetime.now().isoformat()
                }
            print(f"  [FALLBACK] {cef_ticker}: Using fallback data")
        else:
            print(f"  [MISS] {cef_ticker}: No data available")

    holdings_cache = result
    return jsonify(result)


@app.route('/api/holdings/refresh')
def refresh_holdings():
    """Force refresh holdings data from Morningstar."""
    global holdings_cache
    holdings_cache = {}
    return get_all_holdings()


@app.route('/api/config')
def get_config():
    """Return configuration including CEF registry."""
    return jsonify({
        "cefs": list(CEF_REGISTRY.keys()),
        "finnhubKey": os.environ.get("FINNHUB_KEY", ""),
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f">>> CEF NAV Tracker starting on http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
