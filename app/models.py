from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        ('1', 'Hod'),
        ('2','Staff'),
        ('3','Student'),

    )

    user_type = models.CharField(max_length=10, choices=USER, default='1')
    profile_pic = models.ImageField(upload_to='media/profile_pics')
# Create your models here.
