from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.
class MyUser(AbstractUser):
    users_name = models.CharField(max_length=100, null=True, blank=True)




#://django-model-utils.readthedocs.io/en/latest/utilities.html#choices
class Ticket(models.Model):
    NEW = 'NW'
    IN_PROGRESS = 'IP'
    DONE = 'DN'
    INVALID = 'IVD'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),

    ]
    title = models.CharField(max_length=100)
    time = models.DateTimeField(default=now)
    description = models.TextField()
    user_name = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_name')
    ticket_status = models.CharField(choices=STATUS_CHOICES, default=NEW, max_length=3)


    def __str__(self):
        return self.title
