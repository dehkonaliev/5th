from django.shortcuts import render
from django.views import View
from .models import CustomUser

class SignUpView(View):
    def get(self, request):
        pass