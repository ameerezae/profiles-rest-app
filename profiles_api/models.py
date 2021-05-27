from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, username, name, age, password=None):
        if not username:
            raise ValueError('You must specify username.')

        user = self.model(username=username, name=name, age=age)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, name, age, password):
        user = self.create_user(username, name, age, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'age']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.username
