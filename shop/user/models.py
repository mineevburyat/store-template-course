from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(
        verbose_name='аватар',
        upload_to='users',
        null=True,
        blank=True)