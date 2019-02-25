# _*_ coding: utf-8 _*_
# @Time     : 15:55
# @Author   : Amir
# @Site     : 
# @File     : signals.py
# @Software : PyCharm


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()