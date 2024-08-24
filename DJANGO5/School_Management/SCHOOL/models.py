from django.db import models
from django.utils import timezone

# Create your models here.
class School(models.Model):
    Name = models.CharField(max_length=100)
    Phone_number = models.IntegerField()
    Address = models.TextField(max_length=200)
    Email = models.EmailField()


    def __str__(self):
        return self.Name

# Create your models here.
# <p>{{ school.name }}</p>
