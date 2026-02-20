import yfinance as yf
import json
import time
from datetime import datetime
import os

# Full list of symbols (141 total)
TICKERS = [
    # CEFs
    "HQL", "HQH", "THQ", "THW", "BMEZ", "GRX",
    # Holdings
    "AMGN", "PCVX", "INSM", "QURE", "REGN", "CRNX", "DNLI", "FULC", "ARGX", "PSNL", "DYN", "RARE", 
    "IMVT", "XENE", "EWTX", "VRTX", "ALNY", "CYTK", "ARWR", "SRPT", "SION", "BHVN", "AXSM",
    "ABT", "PRLD", "DHR", "OCLS", "TECX", "ISRG", "MRK", "LLY", "ABBV", "MDT", "TMO", "BMY", 
    "ISPY", "ZTS", "BDX", "BSX", "HUM", "ELV", "CVS", "UNH", "ARSR", "PODD", "OHI", "NEO", 
    "SBRA", "WELL", "AZN", "ABVX", "NVO", "SNY", "RHHBY", "OXB", "VNT", "LONN", "NAMS",
    "WST", "WXIBF", "IDXX", "DXCM", "GDLMY", "RYTM", "EW", "JNJ", "RGEN", "SONVY", "GNMSF", 
    "EXAS", "THC", "GH", "NBIX", "CI", "OPCH", "TEVA", "COR", "HALO", "POST", "LH", "HCA", 
    "KR", "ZBH", "BRBR", "SJM", "NSRGY", "KRYAY", "COO", "ITGR", "CHE"
]

STATE_FILE = 'prices.json'
BATCH_SIZE = 30  # Optimized for ~1 min cycle
SLEEP_TIME = 12  # Safety buffer
q_idx = 0

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except: return {}
    return {}

def save_state(full_data, stats=None):
    payload = {"data": full_data, "stats": stats}
    with open(STATE_FILE, 'w') as f:
        json.dump(payload, f)

def fetch_high_precision(symbols):
    results = {}
    try:
        batch_obj = yf.Tickers(' '.join(symbols))
        for sym, t_obj in batch_obj.tickers.items():
            try:
                inf = t_obj.info
                state = inf.get('marketState', 'REGULAR')
                lp = inf.get('regularMarketPrice')
                pc = inf.get('regularMarketPreviousClose')
                pct = inf.get('regularMarketChangePercent', 0)
                
                if state in ['PREMARKET', 'PRE']:
                    pre_px = inf.get('preMarketPrice') or lp
                    ref_px = lp or pc
                    if pre_px and ref_px:
                        lp = pre_px
                        pct = ((pre_px - ref_px) / ref_px) * 100
                elif state in ['POSTMARKET', 'POST', 'CLOSED']:
                    post_px = inf.get('postMarketPrice')
                    ref_px = lp or pc
                    if post_px and ref_px:
                        lp = post_px
                        reg_move = inf.get('regularMarketChangePercent', 0)
                        post_move = ((post_px - ref_px) / ref_px) * 100
                        pct = reg_move + post_move

                results[sym] = {
                    "lp": lp, "pc": pc, "chg": pct, "state": state,
                    "ts": datetime.now().strftime("%H:%M:%S")
                }
            except: continue
        return results
    except Exception as e:
        print(f"[{datetime.now()}] Error: {e}")
    return None

def main():
    global q_idx
    print(f"CEF Elite Bot v4.0 (Performance) started.")
    full_state = load_state()
    full_data = full_state.get('data', {})
    
    stats = {
        "last_cycle_s": 75, # Estimated baseline
        "last_sweep": "Initializing...",
        "ticker_count": len(TICKERS)
    }
    
    start_time = time.time()
    
    while True:
        batch = TICKERS[q_idx : q_idx + BATCH_SIZE]
        if not batch:
            # End of cycle
            cycle_duration = time.time() - start_time
            stats = {
                "last_cycle_s": round(cycle_duration, 1),
                "last_sweep": datetime.now().strftime("%H:%M:%S"),
                "ticker_count": len(TICKERS)
            }
            save_state(full_data, stats)
            print(f"--- Full Cycle Complete: {stats['last_cycle_s']}s ---")
            
            q_idx = 0
            start_time = time.time()
            batch = TICKERS[q_idx : q_idx + BATCH_SIZE]
            
        print(f"[{datetime.now()}] Polling {len(batch)} tickers...")
        res = fetch_high_precision(batch)
        if res:
            full_data.update(res)
            save_state(full_data)
            q_idx += BATCH_SIZE
            time.sleep(SLEEP_TIME)
        else:
            time.sleep(10)

if __name__ == "__main__":
    main()
