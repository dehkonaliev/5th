from django import forms
from .models import Furniture

class FurnitureForm(forms.ModelForm):
    model = Furniture
    fields = '__all__'
    