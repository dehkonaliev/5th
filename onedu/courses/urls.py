from django.urls import path
from .views import list, create, update

urlpatterns = [
    path('explore', list, name='explore'),
    path('create', create, name='create'),
    path('update/<int:pk>', update, name='update')
]