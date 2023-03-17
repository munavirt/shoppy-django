from django.db import models
from django.contrib.auth.modes import AbstractBaseUser, BaseUserManager

# Create your models here.

class Accounts(AbstractBaseUser):
    first_name = models.CharFiled