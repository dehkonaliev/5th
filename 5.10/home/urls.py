from django.urls import path
from .views import CreateList

urlpatterns = [
    path('posts/', CreateList.as_view())
]