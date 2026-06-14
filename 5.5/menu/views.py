from django.shortcuts import render
from django.views import View
from .models import Menu

class ListView(View):
    def get(self, request):
        objects = Menu.objects.all()
        return render(request, 'menu.html', {'menus':objects})
