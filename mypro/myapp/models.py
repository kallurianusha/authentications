from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group

# Create your models here.
class user(AbstractUser):
    email =models.EmailField(unique=True)
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=150,unique=True)
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='user_set_permissions',
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='user_set_groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    def __str__(self):
        return self.username