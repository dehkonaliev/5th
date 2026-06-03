from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='watches/', default='watch_default.jpg', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
