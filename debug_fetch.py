import requests
import json

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=AAPL,AMGN"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    print(f"Fetching: {url}")
    r = requests.get(url, headers=headers)
    print(f"Status Code: {r.status_code}")
    print(f"Headers: {dict(r.headers)}")
    data = r.json()
    print("Response Data (Truncated):")
    print(json.dumps(data, indent=2)[:500])
    
    if 'quoteResponse' in data and 'result' in data['quoteResponse']:
        print(f"Success! Found {len(data['quoteResponse']['result'])} results.")
    else:
        print("Error: quoteResponse/result missing from response.")
except Exception as e:
    print(f"Fetch failed: {e}")
