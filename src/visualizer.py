import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (14, 6)

def plot_price_with_moving_averages(df, stock_name):
    plt.figure()
    plt.plot(df['Date'], df['Close'], label='Close Price', color='black')
    plt.plot(df['Date'], df['SMA_20'], label='SMA 20', color='blue')
    plt.plot(df['Date'], df['EMA_20'], label='EMA 20', color='green')
    plt.title(f"{stock_name} - Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_rsi(df, stock_name):
    plt.figure()
    plt.plot(df['Date'], df['RSI_14'], label='RSI 14', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"{stock_name} - RSI Indicator")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_macd(df, stock_name):
    plt.figure()
    plt.plot(df['Date'], df['MACD'], label='MACD', color='blue')
    plt.plot(df['Date'], df['MACD_signal'], label='Signal Line', color='orange')
    plt.title(f"{stock_name} - MACD")
    plt.xlabel("Date")
    plt.ylabel("MACD Value")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
