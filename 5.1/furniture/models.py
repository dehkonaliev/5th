from django.db import models


class Furniture(models.Model):
    CATEGORIES = (
        ('sofas', 'Sofas'),
        ('lights','Lights'),
        ('tables', 'Tables'),
        ('beds', 'Beds'),
        ('chairs', 'Chairs')
    )
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    info = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='furniture/', default='furniture_default.jpg', blank=True)
    category = models.CharField(max_length=30, choices=CATEGORIES)