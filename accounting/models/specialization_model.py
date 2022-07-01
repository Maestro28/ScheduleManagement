from django.db import models


# Create your models here.


class Specialization(models.Model):
    """
        This class represents a user Specializations.
    """
    name = models.CharField(max_length=20, unique=True)


    def __str__(self):
        """
        Magic method is redefined to show information about Specialization.
        :return: specification name
        """
        return str(self.name)

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Specialization object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
