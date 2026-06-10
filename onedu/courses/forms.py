from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=30)
    duration = forms.IntegerField()
    
    class Meta:
        model = Course
        fields = ['title', 'subject', 'duration']