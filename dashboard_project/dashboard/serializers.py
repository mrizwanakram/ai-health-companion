# dashboard/serializers.py
from rest_framework import serializers
from .models import Metric, Insight

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ['id', 'name', 'value', 'timestamp']

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = ['id', 'metric', 'insight_text', 'created_at']
