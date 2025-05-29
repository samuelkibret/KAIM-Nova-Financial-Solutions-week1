import pandas as pd

class EDA:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def headline_length_stats(self):
        return self.df['headline'].str.len().describe()

    def article_count_by_publisher(self):
        return self.df['publisher'].value_counts()

    def articles_over_time(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        return self.df['date'].dt.date.value_counts().sort_index()
