# sentiment_agent.py
from transformers import pipeline

class SentimentAgent:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def analyze_sentiment(self, journal_entry):
        sentiment = self.sentiment_analyzer(journal_entry['entry'])[0]
        return {
            'sentiment': sentiment['label'],
            'confidence': sentiment['score']
        }
