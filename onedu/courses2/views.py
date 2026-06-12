from django.shortcuts import render, redirect
from courses.forms import CourseForm
from courses.models import Course
from django.views import View

class CreateView(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'course-create.html', {'form':form})
    
    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('course-list')
        return render(request, 'course-create.html', {'form':form})
    
    
class ListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'course-list.html', {'courses':courses})
