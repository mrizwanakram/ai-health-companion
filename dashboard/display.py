# display.py
from insights_aggregation.aggregator import InsightsAggregator
from data_integration.mock_data import mock_data

def display_insights():
    aggregator = InsightsAggregator()
    aggregated_insights = aggregator.aggregate(mock_data['metrics'], [
        {"date": "2024-11-22", "entry": "Feeling stressed but excited."},
        {"date": "2024-11-21", "entry": "Great day, feeling accomplished!"}
    ])
    
    return aggregated_insights
