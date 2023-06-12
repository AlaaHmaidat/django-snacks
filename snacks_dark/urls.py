from django.contrib import admin
from django.urls import path
from .views import DarkPageView

urlpatterns = [
    path('dark', DarkPageView.as_view(), name='dark'),
]
