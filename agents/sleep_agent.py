class SleepAgent:
    def analyze_sleep(self, metrics):
        sleep_insights = []
        for data in metrics:  # Iterate over the list of metrics
            # Ensure data is a dictionary with keys like 'sleep_hours'
            sleep_hours = data['sleep_hours']
            
            # Example logic for sleep insights
            if sleep_hours < 7:
                sleep_insights.append("Try to aim for at least 7-8 hours of sleep for better health.")
            if sleep_hours > 9:
                sleep_insights.append("Consider reducing sleep hours for optimal daytime performance.")
            
        return sleep_insights
