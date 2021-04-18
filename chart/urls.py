from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('chart_bar', views.chart_bar, name="chart_bar"),
    path('chart_bar2', views.chart_bar2, name="chart_bar2"),
    path('chart_bar3', views.chart_bar3, name="chart_bar3"),
]
