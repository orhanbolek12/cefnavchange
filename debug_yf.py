import yfinance as yf
import json

symbols = ["AAPL", "AMGN", "PCVX"]

try:
    print(f"Fetching: {symbols}")
    # Fetch data using yfinance download (handles batches well)
    data = yf.download(symbols, period="1d", interval="1m", progress=False)
    
    if not data.empty:
        print("Success! Data received.")
        print("Columns:", data.columns.tolist())
        print("Data Preview (Close prices):")
        if 'Close' in data:
            print(data['Close'].tail())
        else:
            print(data.tail())
    else:
        print("Error: DataFrame is empty.")
except Exception as e:
    print(f"Library fetch failed: {e}")
