from django.db import models

from accounting.models.user_model import CustomUser
from .procedure_model import Procedure

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=20)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments')
    specialist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='all_appointments')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField(editable=False)

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
