import email
from django.db import models

# Create your models here.
class Consultation(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Consultation request from {self.name} on {self.preferred_date}"

class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'User account with name: {self.name} and email: {self.email} was created'

