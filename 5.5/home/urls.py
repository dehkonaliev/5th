from django.urls import path
from .views import HomeView, AboutView, ChefsView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('chefs', ChefsView.as_view(), name='chefs'),
    path('contact', ContactView.as_view(), name='contact')
]