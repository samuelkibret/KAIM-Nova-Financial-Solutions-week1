from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

class TextAnalysis:
    def __init__(self, df):
        self.df = df
        self.stop_words = set(stopwords.words('english'))

    def get_top_keywords(self, n=20):
        all_text = ' '.join(self.df['headline'].dropna())
        words = re.findall(r'\b\w+\b', all_text.lower())
        words = [word for word in words if word not in self.stop_words]
        return Counter(words).most_common(n)
