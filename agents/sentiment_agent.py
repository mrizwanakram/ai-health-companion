from transformers import pipeline

def sentiment_analysis(journal_entries):
    """
    Perform sentiment analysis on user journal entries.
    Args:
        journal_entries (list): List of dictionaries with journal entries.
    Returns:
        dict: Sentiment summary and suggestions.
    """
    sentiment_analyzer = pipeline("sentiment-analysis")
    sentiments = [sentiment_analyzer(entry['entry'])[0] for entry in journal_entries]
    positive_count = sum(1 for s in sentiments if s['label'] == "POSITIVE")
    negative_count = len(sentiments) - positive_count


