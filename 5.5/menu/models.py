from django.db import models

class Menu(models.Model):
    CATEGORIES = (
        ('breakfast','Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner','Dinner')
    )
    
    name = models.CharField(max_length=70)
    category = models.CharField(max_length=20)
    summ = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, choices=CATEGORIES)
    
    def __str__(self):
        return self.name
    

