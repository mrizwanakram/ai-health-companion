import numpy as np

def sleep_analysis(metrics):
    """
    Analyze sleep data to detect patterns and provide suggestions.
    Args:
        metrics (list): List of dictionaries containing sleep data.
    Returns:
        dict: Insights and recommendations for sleep.
    """
    avg_sleep = np.mean([day['sleep_hours'] for day in metrics])
    suggestion = (
        "You're getting enough sleep. Keep it up!"
        if avg_sleep >= 7
        else "Consider improving your sleep routine to get at least 7 hours per night."
    )
    return {
        "average_sleep_hours": avg_sleep,
        "suggestion": suggestion,
    }
