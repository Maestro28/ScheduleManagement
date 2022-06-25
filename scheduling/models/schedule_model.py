from django.db import models

from accounting.models.user_model import CustomUser
from scheduling.models.location_model import Location


# Create your models here.


class Schedule(models.Model):
    start_datetime = models.DateTimeField(editable=False)
    end_datetime = models.DateTimeField(editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='schedules')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='schedules')

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return str(self.id)

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'