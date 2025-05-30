import pandas as pd
import matplotlib.pyplot as plt

class TimeSeriesAnalysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        # 🛠 Fix: support mixed datetime formats (with or without timezone)
        self.df['date'] = pd.to_datetime(self.df['date'], format='mixed', errors='coerce')
        self.df['date'] = self.df['date'].dt.tz_localize(None)

    def publication_trends_daily(self):
        return self.df['date'].dt.date.value_counts().sort_index()

    def publication_by_hour(self):
        return self.df['date'].dt.hour.value_counts().sort_index()

    def rolling_avg_publication(self, window=7):
        daily_counts = self.df['date'].dt.date.value_counts().sort_index()
        return pd.Series(daily_counts).rolling(window=window).mean()
