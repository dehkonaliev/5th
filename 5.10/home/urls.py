from django.urls import path
from .views import CreateList, DetailUpdateDelete

urlpatterns = [
    path('posts/', CreateList.as_view()),
    path('detail/<int:pk>', DetailUpdateDelete.as_view())
]