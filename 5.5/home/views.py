from django.shortcuts import render
from django.views import View
from .models import Chef, About, Contact
from menu.models import Menu


class HomeView(View):
    def get(self, request):
        chefs = Chef.objects.all().order_by('-id')[:3]
        menus = Menu.objects.all().order_by('-id')[:6]
        about = About.objects.all().first()
        menus_2, menus_all = menus[:2], menus[2:]
        main_chef = Chef.objects.filter(position='main').first()
        context = {
            'chefs':chefs,
            'menus_2':menus_2,
            'menus':menus_all,
            'main_chef':main_chef,
            'about':about
        }
        return render(request, 'index.html', context)
    
    
class AboutView(View):
    def get(self, request):
        chefs = Chef.objects.all().order_by('-id')[:3]
        about = About.objects.all().first()
        main_chef = Chef.objects.filter(position='main').first()
        context = {
            'chefs':chefs,
            'main_chef':main_chef,
            'about':about
        }
        return render(request, 'about.html', context)
    

class ChefsView(View):
    def get(self, request):
        chefs = Chef.objects.all().order_by('-id')[:3]
        context = {
            'chefs':chefs,
        }
        return render(request, 'team.html', context)
    
class ContactView(View):
    def get(self, request):
        contact = Contact.objects.all().first()
        context = {'contact':contact}
        return render(request, 'contact.html', context)