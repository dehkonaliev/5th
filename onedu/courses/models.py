from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    desc = models.CharField(max_length=1000)
    author = models.CharField(max_length=20)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
