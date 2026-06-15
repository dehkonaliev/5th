from django.db import models

class Chef(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='chefs/', default='chef_default.png', blank=True)
    position = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
