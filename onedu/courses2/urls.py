from django.urls import path
from .views import CreateView, ListView

urlpatterns = [
    path('course-list', ListView.as_view(), name='course-list'),
    path('create-course', CreateView.as_view(), name='create-course')
]