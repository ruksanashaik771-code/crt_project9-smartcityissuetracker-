from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Issue, Notification


@receiver(post_save, sender=Issue)
def create_notification(
        sender,
        instance,
        created,
        **kwargs):

    if not created:

        Notification.objects.create(
            user=instance.user,
            message=f'Your issue "{instance.title}" status is now {instance.status}'
        )