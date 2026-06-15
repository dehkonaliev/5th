from django.shortcuts import render
from django.views import View
from .models import Chef

class HomeView(View):
    def get(self, request):
        chefs = Chef.objects.all()
        return render(request, 'index.html', {'chefs':chefs})