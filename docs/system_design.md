# System Design - Mind-Body Connection Dashboard

## Overview
The Mind-Body Connection Dashboard is a comprehensive tool designed to aggregate, analyze, and present insights related to fitness, sleep, and emotional well-being. It pulls data from various sources, processes it using machine learning models, and provides personalized suggestions to enhance overall health. The dashboard uses **Streamlit** to present the data in an interactive and user-friendly interface.

### Key Components:
1. **Fitness Agent**: Aggregates and processes fitness data, including steps and activity levels.
2. **Sleep Agent**: Analyzes sleep-related data to provide insights on sleep quality.
3. **Sentiment Agent**: Performs sentiment analysis on journal entries to assess emotional well-being.
4. **Insights Aggregation**: Combines the results from the fitness, sleep, and sentiment agents into a cohesive set of insights.
5. **Streamlit Dashboard**: Displays the insights in an interactive, visually appealing dashboard.

## System Architecture

### 1. **Data Flow**
   The system relies on structured data stored in JSON files to simulate user metrics:
   - **Fitness Data**: Includes daily step counts and other fitness-related metrics.
   - **Journal Entries**: Users' daily emotional states and reflections, which are analyzed for sentiment.
   - **Aggregated Insights**: A combination of fitness, sleep, and sentiment analysis results that guide user recommendations.

### 2. **Components**
   - **Fitness Agent** (`agents/fitness_agent.py`): Processes fitness-related data (e.g., steps, calories burned) to provide insights and recommendations.
   - **Sleep Agent** (`agents/sleep_agent.py`): Analyzes sleep data (e.g., hours of sleep, quality of sleep) and provides suggestions for improving sleep hygiene.
   - **Sentiment Agent** (`agents/sentiment_agent.py`): Uses NLP techniques to analyze journal entries and determine the overall sentiment (positive, negative, or neutral).
   - **Insights Aggregation** (`insights/aggregation.py`): Combines the outputs of the fitness, sleep, and sentiment agents into a single set of insights, including personalized suggestions.
   - **Dashboard** (`dashboard/dashboard.py`): The central component that integrates the insights and displays them in a Streamlit dashboard. This also includes custom styling to ensure a visually appealing and interactive user experience.

### 3. **Technologies Used**
- **Python 3.x**: The primary programming language.
- **Streamlit**: Used for building the interactive dashboard.
- **JSON**: The format for storing fitness, journal, and sleep data.
- **Transformers**: Used in the Sentiment Agent for natural language processing (NLP) tasks.
- **Pandas & Numpy**: Used for data manipulation and aggregation tasks.
- **Matplotlib/Plotly (optional)**: Can be used for more complex visualizations if needed.

## Database Schema

In the current design, no relational database is required since the data is provided via static JSON files. However, if the project scales, future improvements may include:

1. **Users Table**:
   - `id`: User ID (Primary Key)
   - `name`: User's name
   - `email`: User's email address
   - `fitness_data`: Reference to fitness data
   - `journal_entries`: Reference to journal entries
   - `sleep_data`: Reference to sleep data

2. **Fitness Data Table**:
   - `user_id`: Reference to User ID
   - `date`: Date of the recorded data
   - `steps`: Steps taken on the day
   - `calories_burned`: Calories burned on the day

3. **Sleep Data Table**:
   - `user_id`: Reference to User ID
   - `date`: Date of the recorded data
   - `hours_slept`: Hours slept on the day
   - `sleep_quality`: Rating of sleep quality

4. **Journal Entries Table**:
   - `user_id`: Reference to User ID
   - `entry_date`: Date of the entry
   - `entry_text`: Text content of the journal entry
   - `sentiment`: Sentiment of the journal entry (positive, negative, or neutral)

## Key Features
- **Personalized Insights**: Based on fitness, sleep, and sentiment data, personalized suggestions are provided to users for improvement.
- **Interactive Dashboard**: A user-friendly dashboard created using Streamlit, with real-time updates based on data.
- **Visualization**: Displays metrics in a readable and insightful format, with charts, progress bars, and emoji-based suggestions.

## Future Enhancements
- **User Authentication**: Integrating a user authentication system to manage multiple users and their data securely.
- **Database Integration**: Switching from static JSON files to a database for more dynamic, scalable data storage.
- **AI Integration**: Implementing more sophisticated AI models for deeper insights (e.g., predictive health analytics, more advanced sentiment analysis).
- **Mobile App Version**: Adapting the dashboard for mobile use to allow users to track their progress on the go.
