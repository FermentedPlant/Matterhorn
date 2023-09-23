from django.db import models
from django.utils import timezone
from . manager import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 15, unique = True)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 25)
    balance = models.DecimalField(max_digits = 12, decimal_places = 3, default = 0, null = True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    # Initialize Custom Manager
    objects = CustomUserManager()

    # A string describing the name of the field on the user model that is used as the unique identifier. 
    # DEFAULT : USERNAME_FIELD = "username"
    USERNAME_FIELD = 'email'        

    # A list of the field names that will be prompted for when creating a user via the createsuperuser. 
    # DEFAULT : REQUIRED_FIELDS = ["email"]
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']   

    def __str__(self):
        return self.username
