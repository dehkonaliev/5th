from django.shortcuts import render, redirect
from django.views import View
from .models import Furniture
from .forms import FurnitureForm


class FurnitureView(View):
    def get(self, request):
        objects = Furniture.objects.all().order_by('-id')
        return render(request, 'furniture.html', {'objects':objects})
    
class DetailView(View):
    def get(self, request, pk):
        object = Furniture.objects.filter(id=pk).first()
        return render(request, 'furniture_detail.html', {'object':object})
    
    
class UpdateView(View):
    def get(self, request, pk):
        object = Furniture.objects.filter(id=pk).first()
        form = FurnitureForm(instance=object)
        return render(request, 'furniture_update.html', {'form':form, 'object':object})
    
    def post(self, request, pk):
        object = Furniture.objects.filter(pk=pk).first()
        form = FurnitureForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('furniture_detail', pk=object.pk)
        return render(request, 'furniture_update.html', {'form':form, 'object':object})
    
class CreateView(View):
    def get(self, request):
        form = FurnitureForm()
        return render(request, 'furniture_create.html', {'form':form})
    
    def post(self, request):
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('furniture')
        
