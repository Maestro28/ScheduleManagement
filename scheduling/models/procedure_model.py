from django.db import models

from auth.models.specialization_model import Specialization

# Create your models here.


class Procedure(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(max_length=20)
    spec = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='procedures')




    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return str(self.name)

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
