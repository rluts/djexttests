from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    Users properties
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    about = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )

    
class Event(models.Model):

    name = models.CharField(
        max_length=500
    )
    
    trainer = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE
    )