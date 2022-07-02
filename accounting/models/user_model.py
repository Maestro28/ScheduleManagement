from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email
from phone_field import PhoneField

from accounting.managers import CustomUserManager
from .specialization_model import Specialization
from accounting.validators import validate_phone_number

# Create your models here.



# Create your models here.

ROLE_CHOICES = ( # change tu Enum
    (0, 'visitor'),
    (1, 'admin'),
    (2, 'worker'),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
        This class represents a basic user.
    """
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=16, unique=True, validators=[validate_phone_number])
    password = models.CharField(max_length=128)
    specs = models.ManyToManyField(Specialization, related_name='users', blank=True)
    role = models.IntegerField(default=0, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = CustomUserManager()

    ordering = ('email',)

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        if self.role == 1:
            return True
        return False

    def __str__(self):
        """
        Magic method is redefined to show information about CustomUser.
        :return: user email
        """
        return str(self.email)

    def __repr__(self):
        """
        This magic method is redefined to show class and id of CustomUser object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"



