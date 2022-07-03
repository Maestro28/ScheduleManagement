from django.contrib.auth.base_user import BaseUserManager

# from .models.user_model import CustomUser


class CustomUserManager(BaseUserManager):
    def create_user(self, **kwargs):  # -> CustomUser:
        """
        Creates and saves a User with the given email and password.
        :param: email post address of user
        :param: first_name user fist name
        :param: last_name user last name
        :param: specs user specializations
        :param: password user password
        :param: role user role
        :param: is_active user active status
        """

        email = kwargs.pop('email') if kwargs.get('email') else None

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        if kwargs.get('first_name'):
            first_name = kwargs.pop('first_name')
            user.first_name = first_name
        if kwargs.get('last_name'):
            last_name = kwargs.pop('last_name')
            user.last_name = last_name
        if kwargs.get('phone'):
            phone = kwargs.pop('phone')
            user.phone = phone
        if kwargs.get('role', 0):
            role = kwargs.pop('role')
            user.role = role
        if kwargs.get('password'):
            password = kwargs.pop('password')
            user.set_password(password)
            user.is_active = True
        user.save(using=self._db)
        if kwargs.get('specs') and user.role == 2:
            specs = kwargs.pop('specs')
            for spec in specs:
                user.specs.add(spec)
        return user

    def create_superuser(self, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user( **kwargs)

        user.role = 1
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
