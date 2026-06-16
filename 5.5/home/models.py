from django.db import models

class Chef(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='chefs/', default='chef_default.png', blank=True)
    position = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class About(models.Model):
    years = models.IntegerField()
    clients = models.IntegerField()
    awards = models.IntegerField()
    events = models.IntegerField()
    
class Contact(models.Model):
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.email
