import numpy as np

def fitness_analysis(metrics):
    """
    Analyze activity data to provide insights and suggestions.
    Args:
        metrics (list): List of dictionaries containing steps, calories burned, etc.
    Returns:
        dict: Insights and suggestions for fitness.
    """
    total_steps = sum(day['steps'] for day in metrics)
    avg_steps = total_steps / len(metrics)
    suggestion = (
        "Great job! Keep maintaining your activity level."
        if avg_steps >= 10000
        else "Try increasing your daily steps to reach the recommended 10,000 steps per day."
    )
    return {
        "total_steps": total_steps,
        "average_steps": avg_steps,
        "suggestion": suggestion,
    }
