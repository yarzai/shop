from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)

from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValidationError("Email is required.")
        if not name:
            raise ValidationError("Name is required.")
        if not password:
            raise ValidationError("Password is required.")

        user = self.model(email=email, name=name)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to="profiles", null=True, blank=True)
    remember_me = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()

    class Meta:
        db_table = 'accounts'
