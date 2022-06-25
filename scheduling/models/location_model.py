from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        """
        Magic method is redefined to show information about Location.
        :return: location name
        """
        return str(self.name)

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Location object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
