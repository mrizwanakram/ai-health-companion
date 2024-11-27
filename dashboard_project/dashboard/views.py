# dashboard/views.py
from django.shortcuts import render
from .models import Metric, Insight

def dashboard_view(request):
    metrics = Metric.objects.all()
    insights = Insight.objects.all()
    return render(request, 'dashboard/dashboard.html', {'metrics': metrics, 'insights': insights})



# dashboard/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Metric, Insight
from .serializers import MetricSerializer, InsightSerializer

class MetricList(APIView):
    def get(self, request):
        metrics = Metric.objects.all()
        serializer = MetricSerializer(metrics, many=True)
        return Response(serializer.data)

class InsightList(APIView):
    def get(self, request):
        insights = Insight.objects.all()
        serializer = InsightSerializer(insights, many=True)
        return Response(serializer.data)
