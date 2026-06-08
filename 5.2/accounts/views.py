from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import UserForm

class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'sign-up.html', {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')