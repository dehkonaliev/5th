from django.urls import path
from .views import SignUpView, HomeView, LoginView, LogoutView, ChangePasswordView, ProfileView, ProfileUpdate
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in', LoginView.as_view(), name='sign-in'),
    path('sign-out', LogoutView.as_view(), name='sign-out'),
    path('change-password', ChangePasswordView.as_view(), name='change-pass'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('update', ProfileUpdate.as_view(), name='update')
]