# scripts/sentiment.py

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure the lexicon is downloaded
nltk.download('vader_lexicon', quiet=True)

# Initialize the analyzer
sia = SentimentIntensityAnalyzer()

def get_sentiment_score(text):
    """Returns the compound sentiment score of a text using VADER."""
    return sia.polarity_scores(text)['compound']

def get_sentiment_label(score):
    """Classifies sentiment based on VADER compound score."""
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_sentiment(csv_path: str, output_path: str):
    """
    Loads reviews from a CSV, computes sentiment score and label, saves new DataFrame.
    
    Parameters:
        csv_path (str): Path to raw reviews CSV.
        output_path (str): Path to save processed reviews CSV.
    """
    df = pd.read_csv(csv_path)

    # Drop rows without a review
    df = df.dropna(subset=['Translated_Review'])

    # Apply VADER
    df['sentiment_score'] = df['Translated_Review'].apply(get_sentiment_score)
    df['sentiment_label'] = df['sentiment_score'].apply(get_sentiment_label)

    # Save processed DataFrame
    df.to_csv(output_path, index=False)
    print(f"Sentiment data saved to: {output_path}")

    return df
