from django.urls import path
from .views import WatchView

urlpatterns = [
    path('', WatchView.as_view(), name='watches')
]