from django.urls import path
from .views import FurnitureView, DetailView, UpdateView

urlpatterns = [
    path('', FurnitureView.as_view(), name='furniture'),
    path('update/<int:pk>', UpdateView.as_view(), name='furniture_update'),
    path('detail/<int:pk>', DetailView.as_view(), name='furniture_detail'),
]