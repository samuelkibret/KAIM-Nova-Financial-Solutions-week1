# text_analysis.py (inside src/ folder)

import pandas as pd
import string
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os

# Ensure NLTK data is available and paths are configured
nltk.download('punkt', download_dir='./nltk_data')
nltk.download('stopwords', download_dir='./nltk_data')
nltk.data.path.append(os.path.abspath('./nltk_data'))

class TopicModeling:
    def __init__(self, df: pd.DataFrame, text_column: str):
        self.df = df.copy()
        self.text_column = text_column
        self.stop_words = set(stopwords.words('english'))
        self.punctuation_table = str.maketrans('', '', string.punctuation)

    def preprocess_text(self, text: str):
        if pd.isna(text):
            return []
        # Tokenize
        tokens = word_tokenize(text.lower())
        # Remove punctuation and non-alpha
        cleaned = [word.translate(self.punctuation_table) for word in tokens if word.isalpha()]
        # Remove stopwords and short tokens
        filtered = [word for word in cleaned if word not in self.stop_words and len(word) > 2]
        return filtered

    def extract_common_keywords(self, top_n=20):
        all_tokens = []
        for text in self.df[self.text_column]:
            all_tokens.extend(self.preprocess_text(text))
        counter = Counter(all_tokens)
        return counter.most_common(top_n)
