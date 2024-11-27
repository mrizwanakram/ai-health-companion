# aggregator.py
from agents.fitness_agent import FitnessAgent
from agents.sleep_agent import SleepAgent
from agents.sentiment_agent import SentimentAgent

class InsightsAggregator:
    def __init__(self):
        self.fitness_agent = FitnessAgent()
        self.sleep_agent = SleepAgent()
        self.sentiment_agent = SentimentAgent()

    def aggregate(self, metrics, journal_entries):
        fitness_insights = self.fitness_agent.analyze_activity(metrics)
        sleep_insights = self.sleep_agent.analyze_sleep(metrics)
        sentiment_insights = [self.sentiment_agent.analyze_sentiment(entry) for entry in journal_entries]
        
        return {
            'fitness_insights': fitness_insights,
            'sleep_insights': sleep_insights,
            'sentiment_insights': sentiment_insights
        }
