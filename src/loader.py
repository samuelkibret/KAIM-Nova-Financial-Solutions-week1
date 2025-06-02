import pandas as pd
import os

def load_stock_data(tickers, data_path="../data/raw_data/yfinance_data"):
    """
    Load historical stock data for given tickers from CSV files.
    
    Args:
        tickers (list): List of stock ticker symbols (e.g., ['AAPL', 'AMZN'])
        data_path (str): Path to the directory containing CSV files
    
    Returns:
        dict: Dictionary with tickers as keys and DataFrames as values
    """
    stock_data = {}
    for ticker in tickers:
        file_path = os.path.join(data_path, f"{ticker}_historical_data.csv")
        stock_data[ticker] = pd.read_csv(file_path)
    return stock_data