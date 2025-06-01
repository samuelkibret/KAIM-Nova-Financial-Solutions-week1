# src/text_analysis.py

import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

class TextAnalysis:
    """
    Simple text cleaning and keyword extraction WITHOUT NLTK.
    - Lowercase
    - Remove digits
    - Remove punctuation
    - Split on whitespace
    - Use CountVectorizer(stop_words='english') to extract top keywords/phrases
    """

    def __init__(self, df, text_column='headline'):
        """
        Parameters:
          df (pd.DataFrame): DataFrame with a column of raw text.
          text_column (str): Name of that text column (e.g., 'headline').
        """
        self.df = df.copy()
        self.text_column = text_column
        self.cleaned = False

    def clean_text(self):
        """
        1) Lowercase
        2) Remove digits
        3) Remove punctuation (keep spaces)
        4) Split on whitespace implicitly via CountVectorizer later
        Stores result in self.df['cleaned_text'].
        """
        def preprocess(text):
            txt = str(text).lower()
            txt = re.sub(r'\d+', '', txt)            # remove digits
            txt = re.sub(r'[^\w\s]', '', txt)         # remove punctuation
            return txt

        self.df['cleaned_text'] = self.df[self.text_column].fillna("").apply(preprocess)
        self.cleaned = True

    def extract_keywords(self, max_features=1000, ngram_range=(1, 2)):
        """
        Builds a CountVectorizer (unigrams + bigrams, with built-in English stopwords),
        then returns the vocabulary (keywords/phrases) as an array of strings.
        """
        if not self.cleaned:
            self.clean_text()

        vectorizer = CountVectorizer(
            stop_words='english',
            max_features=max_features,
            ngram_range=ngram_range
        )
        dtm = vectorizer.fit_transform(self.df['cleaned_text'])
        return vectorizer.get_feature_names_out()
