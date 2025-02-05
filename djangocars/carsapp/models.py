from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Signup(AbstractUser):
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)