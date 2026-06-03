from django.shortcuts import render
from django.views import View
from .models import Watch

class WatchView(View):
    def get(self, request):
        objects = Watch.objects.all()
        return render(request, 'watches.html', {'objects':objects})
