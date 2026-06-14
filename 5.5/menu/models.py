from django.db import models

class Menu(models.Model):    
    name = models.CharField(max_length=70)
    summ = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menus/', blank=True, default='menu_default.jpg')
    
    def __str__(self):
        return self.name
    

