import sys
import os
import streamlit as st
import json

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from insights.aggregation import aggregate_insights

# Load mock data
with open("data/mock_data.json", "r") as f:
    fitness_data = json.load(f)['metrics']

with open("data/sample_journal_entries.json", "r") as f:
    journal_entries = json.load(f)['journal_entries']

# Perform insights aggregation
insights = aggregate_insights(fitness_data, fitness_data, journal_entries)

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #2E8B57;
        font-weight: bold;
    }
    .header {
        font-size: 24px;
        color: #4682B4;
        font-weight: bold;
    }
    .section {
        padding: 20px;
        background-color: #F5F5F5;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .suggestion {
        font-size: 18px;
        font-style: italic;
        color: #FF6347;
    }
    .positive {
        color: #32CD32;
        font-size: 20px;
    }
    .negative {
        color: #FF6347;
        font-size: 20px;
    }
    .emoji {
        font-size: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit Dashboard
st.markdown('<div class="title">Mind-Body Connection Dashboard</div>', unsafe_allow_html=True)

# Fitness Insights
st.markdown('<div class="header">🏃‍♂️ Fitness Insights</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write(f"**Total Steps:** {insights['fitness']['total_steps']} 🚶‍♂️")
    st.write(f"**Average Steps:** {insights['fitness']['average_steps']} 👣")
    
    # Fix the progress value to ensure it's between 0.0 and 1.0
    progress_value = min(insights['fitness']['total_steps'] / 10000, 1.0)  # Ensures max value is 1.0
    st.progress(progress_value)  # Assuming 10,000 steps is the target goal
    
    st.markdown(f'<div class="suggestion">{insights["fitness"]["suggestion"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Sleep Insights
st.markdown('<div class="header">😴 Sleep Insights</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write(f"**Average Sleep Hours:** {insights['sleep']['average_sleep_hours']} 🛏️")
    
    # Adding a slider for sleep improvement
    st.slider('Improve Sleep Goal: Hours per night', 6, 10, value=int(insights['sleep']['average_sleep_hours']))
    
    st.markdown(f'<div class="suggestion">{insights["sleep"]["suggestion"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Sentiment Analysis
st.markdown('<div class="header">🧠 Sentiment Analysis</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write(f"**Positive Journal Entries:** {insights['sentiment']['positive_entries']} 😊")
    st.write(f"**Negative Journal Entries:** {insights['sentiment']['negative_entries']} 😔")
    
    # Adding color-coded suggestions
    if insights['sentiment']['positive_entries'] > insights['sentiment']['negative_entries']:
        st.markdown(f'<div class="positive">You seem to be in a positive mindset! Keep it up! 🎉</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="negative">There are some challenges. Consider mindfulness or journaling. 🌱</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="suggestion">{insights["sentiment"]["suggestion"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Overall Suggestion
st.markdown('<div class="header">🌟 Overall Suggestion</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown(f'<div class="suggestion">{insights["overall_suggestion"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Add a button for user interaction
if st.button('Get More Tips 🧘‍♀️'):
    st.write("Here's a quick tip: Take 5 minutes each day to focus on deep breathing or meditation. It helps with overall well-being!")
