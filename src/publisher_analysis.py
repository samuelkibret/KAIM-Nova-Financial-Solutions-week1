# src/publisher_analysis.py
import pandas as pd

class PublisherAnalysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def top_publishers(self, n=10):
        """Top N publishers by article count"""
        return self.df['publisher'].value_counts().head(n)

    def publisher_article_distribution(self):
        """Article count per publisher"""
        return self.df['publisher'].value_counts()

    def unique_email_domains(self):
        """Extract domain names if publisher is an email"""
        self.df['domain'] = self.df['publisher'].dropna().apply(
            lambda x: x.split('@')[-1] if '@' in x else None
        )
        return self.df['domain'].value_counts(dropna=True)
