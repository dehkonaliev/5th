from django.shortcuts import render
from django.views import View
from .models import Chef
from menu.models import Menu


class HomeView(View):
    def get(self, request):
        chefs = Chef.objects.all().order_by('-id')[:3]
        menus = Menu.objects.all().order_by('-id')[:6]
        menus_2, menus_all = menus[:2], menus[2:]
        main_chef = Chef.objects.filter(position='main').first()
        context = {
            'chefs':chefs,
            'menus_2':menus_2,
            'menus':menus_all,
            'main_chef':main_chef
        }
        return render(request, 'index.html', context)