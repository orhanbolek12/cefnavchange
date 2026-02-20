import yfinance as yf
import json

sym = "AMGN"

try:
    print(f"Investigating {sym}...")
    t = yf.Ticker(sym)
    
    # 1. fast_info
    fi = t.fast_info
    print("--- FAST INFO ---")
    print(f"Last Price: {fi.last_price}")
    print(f"Prev Close: {fi.previous_close}")
    print(f"Calc Chg: {((fi.last_price - fi.previous_close) / fi.previous_close)*100 if fi.previous_close else 0}%")
    
    # 2. info (Real-time and metadata)
    print("\n--- INFO DICT (Keys available) ---")
    inf = t.info
    interesting_keys = [
        'regularMarketPrice', 'regularMarketPreviousClose', 'regularMarketChangePercent',
        'preMarketPrice', 'preMarketChangePercent', 'postMarketPrice', 'postMarketChangePercent',
        'currentPrice', 'targetMeanPrice', 'recommendationKey', 'marketState'
    ]
    for k in interesting_keys:
        if k in inf:
            print(f"{k}: {inf[k]}")
        else:
            print(f"{k}: N/A")

except Exception as e:
    print(f"Error: {e}")
