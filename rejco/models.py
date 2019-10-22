from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    owner = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    dispatched = models.BooleanField(max_length=200)
    arrived = models.BooleanField(max_length=200)
    arrival_time = models.DateTimeField(auto_now=True)
