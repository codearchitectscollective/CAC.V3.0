from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Profile

#when user is saved send this signal
#reciever is this create profile function 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        default_image_filename = 'default.png'  # Filename of the default image
        Profile.objects.create(user=instance, image=default_image_filename)
   
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    instance.profile.save()

#import in apps.py 