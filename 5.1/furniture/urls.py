from django.urls import path
from .views import FurnitureView, DetailView

urlpatterns = [
    path('', FurnitureView.as_view(), name='furniture'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail')
]