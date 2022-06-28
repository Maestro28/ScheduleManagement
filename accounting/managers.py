from django.contrib.auth.base_user import BaseUserManager

# from .models.user_model import CustomUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email,  # first_name, last_name, phone,
                    password=None, role=0, is_active=True, **kwargs):  # -> CustomUser:
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
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **kwargs)
        if kwargs.get('first_name'):
            first_name = kwargs.pop('first_name')
            user.first_name = first_name
        if kwargs.get('last_name'):
            last_name = kwargs.pop('last_name')
            user.last_name = last_name
        if kwargs.get('phone'):
            phone = kwargs.pop('phone')
            user.phone = phone

        user.set_password(password)
        user.save(using=self._db)
        # for s in specs:
        #     user.specs.add(s)
        # user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password, **kwargs)

        if kwargs.get('first_name'):
            first_name = kwargs.pop('first_name')
            user.first_name = first_name
        if kwargs.get('last_name'):
            last_name = kwargs.pop('last_name')
            user.last_name = last_name
        if kwargs.get('phone'):
            phone = kwargs.pop('phone')
            user.phone = phone

        user.role = 1
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
