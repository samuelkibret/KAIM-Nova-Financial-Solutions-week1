import pandas as pd

class TimeSeriesAnalysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.df['date'] = pd.to_datetime(self.df['date'])

    def publication_trends_daily(self):
        """Articles published per day"""
        return self.df['date'].dt.date.value_counts().sort_index()

    def publication_by_hour(self):
        """Articles published by hour of day (UTC-4)"""
        return self.df['date'].dt.hour.value_counts().sort_index()

    def rolling_avg_publication(self, window=7):
        """7-day rolling average of article publication count"""
        daily_counts = self.df['date'].dt.date.value_counts().sort_index()
        daily_series = pd.Series(daily_counts)
        return daily_series.rolling(window=window).mean()
