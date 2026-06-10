from django.urls import path
from .views import ListView

urlpatterns = [
    path('explore', ListView.as_view(), name='explore')
]