# dashboard/urls.py
from django.urls import path
from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),

    path('api/metrics/', views.MetricList.as_view(), name='metric-list'),
    path('api/insights/', views.InsightList.as_view(), name='insight-list'),
]
