# app.py
from flask import Flask, render_template
from data_integration import get_steps_data # Get the mock data from data_integration
from fitness_agent import FitnessTrackingAgent
from sleep_agent import SleepAnalysisAgent
from journaling_agent import JournalingSentimentAnalysisAgent
from mock_journals import mock_journals  # Import mock journals

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch mock data from the updated get_steps_data function
    fitbit_data = get_steps_data()
    
    # Run agents
    fitness_agent = FitnessTrackingAgent(fitbit_data)
    fitness_insights = fitness_agent.analyze_activity()
    
    sleep_agent = SleepAnalysisAgent(fitbit_data)
    sleep_insights = sleep_agent.analyze_sleep()
    
    journaling_agent = JournalingSentimentAnalysisAgent(mock_journals)
    mental_health_insights = journaling_agent.analyze_sentiment()
    
    # Aggregate insights
    aggregated_insights = {
        'fitness': fitness_insights,
        'sleep': sleep_insights,
        'mental_health': mental_health_insights
    }
    
    # Render results on a webpage
    return render_template('index.html', insights=aggregated_insights)

if __name__ == '__main__':
    app.run(debug=True)
