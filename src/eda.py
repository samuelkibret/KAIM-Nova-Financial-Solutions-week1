import pandas as pd
import matplotlib.pyplot as plt

class EDA:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def headline_length_stats(self):
        return self.df['headline'].str.len().describe()

    def article_count_by_publisher(self):
        return self.df['publisher'].value_counts()

    def articles_over_time(self):
    # Step 1: Parse all dates, allow coercion of bad ones
        self.df['date'] = pd.to_datetime(self.df['date'], format="mixed", errors='coerce')

        # Step 2: Remove timezone info (if any)
        self.df['date'] = self.df['date'].dt.tz_localize(None)

        # Step 3: Extract date only (drop time)
        self.df['date'] = self.df['date'].dt.date

        # Step 4: Plot number of articles over time
        articles_by_date = self.df['date'].value_counts().sort_index()

        plt.figure(figsize=(12, 6))
        articles_by_date.plot(kind='bar')
        plt.title("Number of Articles Published Over Time")
        plt.xlabel("Date")
        plt.ylabel("Number of Articles")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
