from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'sign-up.html', {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'sign-in.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                raise ValueError('The password or username is incorrect!')
            login(request, user)
            return redirect('home')
        
class LogoutView(View):
    def get(self, request):
        return render(request, 'sign-out.html')
    def post(self, request):
        logout(request)
        return redirect('home')
    
class ChangePasswordView(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass