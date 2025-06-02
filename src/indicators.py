import talib as ta

def calculate_indicators(df):
    df['SMA_20'] = ta.SMA(df['Close'], timeperiod=20)
    df['EMA_20'] = ta.EMA(df['Close'], timeperiod=20)
    df['RSI_14'] = ta.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], _ = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['ATR_14'] = ta.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)

    return df
