from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields): 
        "Creates and saves a new user"

        if not phone:
            raise ValueError(_('Users must have an email address'))

        user = self.model(phone=phone, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password):

        "Creates and saves a new superuser"

        user = self.create_user(phone, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"