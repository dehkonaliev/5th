from django.shortcuts import render
from django.views import View
from .models import Furniture
from .forms import FurnitureForm


class FurnitureView(View):
    def get(self, request):
        objects = Furniture.objects.all()
        return render(request, 'furniture.html', {'objects':objects})
    
class DetailView(View):
    def get(self, request, pk):
        object = Furniture.objects.filter(id=pk).first()
        return render(request, 'furniture_detail.html', {'object':object})
    
class ListView(View):
    def get(self, request):
        objects = Furniture.objects.all()
        return render(request, 'furniture_list.html', {'objects':objects})
    
class UpdateView(View):
    def get(self, request, pk):
        object = Furniture.objects.filter(pk=pk).first()
        form = FurnitureForm(instance=object)
        return render(request, 'furniture_update.html', {'form':form, 'object':object})
        
