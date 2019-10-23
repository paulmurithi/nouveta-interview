from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Package(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    dispatched = models.BooleanField(default = False)
    arrived = models.BooleanField(default = False)
    arrival_time = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    viewed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# @receiver(post_save, user=User)
# def create_disppatch_message(sender, **kwargs):
#     if kwargs.get('dispatched', False):
#         Notification.objects.create(title='dispatch', message='your package was dispatched')