class FitnessAgent:
    def analyze_activity(self, metrics):
        activity_insights = []
        for data in metrics:  # Iterate over the list of metrics
            # Assuming 'data' is a dictionary with keys like 'steps', 'heart_rate', etc.
            steps = data['steps']
            heart_rate = data['heart_rate']
            sleep_hours = data['sleep_hours']
            hrv = data['hrv']
            
            # Example logic for fitness insights
            if steps < 8000:
                activity_insights.append("Increase daily steps for better fitness.")
            if heart_rate < 70:
                activity_insights.append("Consider more intense activities to raise heart rate.")
            if sleep_hours < 7:
                activity_insights.append("Aim for at least 7-8 hours of sleep for better recovery.")
            if hrv < 50:
                activity_insights.append("Consider stress management techniques to improve HRV.")
            
        return activity_insights

