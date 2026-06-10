from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)
    category = models.CharField(max_length=20, null=True)
    desc = models.CharField(max_length=1000, null=True)
    author = models.CharField(max_length=20, null=True)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    def __str__(self):
        return self.title
    
