from django.shortcuts import render, redirect
from django.views import View
from .models import Course
from .forms import CourseForm


def list(request):
    courses = Course.objects.all()
    return render(request, 'course-list.html', {'courses':courses})
    
def create(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('explore') 
    return render(request, 'course-create.html', {'form':form})

def update(request, pk):
    course = Course.objects.filter(pk=pk).first()
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(instance=course)
        if form.is_valid():
            form.save()
            return redirect('explore')
        
    return render(request, 'course-update.html', {'form':form})
    
