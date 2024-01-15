from django.db.models.signals import pre_save
from django.dispatch import receiver
from app.models import Book
from django.apps import apps

@receiver(pre_save, sender=Book)
def update_price_on_status_change(sender, instance, **kwargs):
    print(instance.status)


#dajgoirhjagoihroi


def demo():
    print('hello world')