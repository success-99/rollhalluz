from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, birth_day, phone, address, password=None, **extra_fields):
        if not full_name:
            raise ValueError('The Full Name field must be set')
        if not phone:
            raise ValueError('The Phone field must be set')

        user = self.model(
            full_name=full_name,
            birth_day=birth_day,
            phone=phone,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, birth_day, phone, address, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(full_name, birth_day, phone, address, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255, unique=True)
    birth_day = models.IntegerField()
    phone = models.CharField(max_length=9, unique=True)
    address = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELDS = ['birth_day', 'phone', 'address']

    def __str__(self):
        return self.full_name
