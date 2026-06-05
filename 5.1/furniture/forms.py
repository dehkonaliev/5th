from django import forms
from .models import Furniture

class FurnitureForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField()
    info = forms.CharField(max_length=1000)
    image = forms.ImageField(required=False)
    category = forms.CharField(max_length=30)
    
    class Meta:
        model = Furniture
        fields = ['name', 'price', 'info', 'image', 'category']
    