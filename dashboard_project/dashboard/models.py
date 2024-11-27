# dashboard/models.py
from django.db import models



class Metric(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Insight(models.Model):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    insight_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Insight for {self.metric.name}"
