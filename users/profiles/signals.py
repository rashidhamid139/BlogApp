from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@post_save( post_save, sender= User)
def create_user_profile(sender, instance, created, **kwargs ):
    if created:
        pass

@receiver(post_save, sender=User)
def save_user_prodile( sender, instance, **kwargs ):
    instance.profile.save()

    