from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email


from accounting.managers import CustomUserManager
from .specialization_model import Specialization

# Create your models here.



# Create your models here.

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
    (2, 'worker'),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
        This class represents a basic user.
    """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    password = models.CharField(max_length=30)
    # spec = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='users')
    specs = models.ManyToManyField(Specialization, related_name='users', blank=True, null=True)
    role = models.IntegerField(default=0, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'role']

    objects = CustomUserManager()

    ordering = ('email',)

    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at,
                 user role, user is_active
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



