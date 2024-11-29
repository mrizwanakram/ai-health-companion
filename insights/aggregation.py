from agents.fitness_agent import fitness_analysis
from agents.sleep_agent import sleep_analysis
from agents.sentiment_agent import sentiment_analysis

def aggregate_insights(fitness_data, sleep_data, journal_entries):
    """
    Combine insights from fitness, sleep, and sentiment analysis.
    Args:
        fitness_data (list): Fitness metrics.
        sleep_data (list): Sleep metrics.
        journal_entries (list): Journal entries.
    Returns:
        dict: Combined insights.
    """
    fitness_insights = fitness_analysis(fitness_data)
    sleep_insights = sleep_analysis(sleep_data)
    sentiment_insights = sentiment_analysis(journal_entries)

    return {
        "fitness": fitness_insights,
        "sleep": sleep_insights,
        "sentiment": sentiment_insights,
        "overall_suggestion": (
            "Focus on improving your sleep and mood to enhance overall well-being."
            if sleep_insights['average_sleep_hours'] < 7 or sentiment_insights['negative_entries'] > 0
            else "Great balance! Keep maintaining your lifestyle."
        ),
    }
