from django.shortcuts import render
from django.views import View
from .models import Furniture


class FurnitureView(View):
    def get(self, request):
        objects = Furniture.objects.all()
        return render(request, 'furniture.html', {'objects':objects})
    
class DetailView(View):
    def get(self, request, pk):
        object = Furniture.objects.filter(id=pk).first()
        return render(request, 'furniture_detail.html', {'object':object})
