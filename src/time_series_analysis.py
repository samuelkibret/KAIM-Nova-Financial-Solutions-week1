# timeseries.py

import pandas as pd

class TimeSeriesAnalysis:
    def __init__(self, df):
        self.df = df.copy()
        self.preprocess_dates()

    def preprocess_dates(self):
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df['date'] = self.df['date'].apply(
            lambda dt: dt.tz_localize('UTC-4') if dt.tzinfo is None else dt
        )
        self.df['date_utc'] = self.df['date'].dt.tz_convert('UTC')
        self.df['date_naive'] = self.df['date_utc'].dt.tz_localize(None)

        self.df['year'] = self.df['date_naive'].dt.year
        self.df['month'] = self.df['date_naive'].dt.month
        self.df['day'] = self.df['date_naive'].dt.date
        self.df['hour'] = self.df['date_naive'].dt.hour
        self.df['weekday'] = self.df['date_naive'].dt.day_name()

    def group_by_day(self):
        return self.df.groupby('day').size()

    def group_by_month(self):
        return self.df.groupby([self.df['year'], self.df['month']]).size()

    def detect_spikes(self, daily_counts, window=7, threshold=2.0):
        rolling_avg = daily_counts.rolling(window=window).mean()
        return daily_counts[daily_counts > rolling_avg * threshold]

    def hourly_distribution(self):
        return self.df['hour'].value_counts().sort_index()

    def weekday_distribution(self):
        return self.df['weekday'].value_counts()

    def get_dataframe(self):
        return self.df.copy()
