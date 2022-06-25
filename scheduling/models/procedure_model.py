from django.db import models

from accounting.models.specialization_model import Specialization

# Create your models here.


class Procedure(models.Model):
    name = models.CharField(max_length=20)
    # duration = models.PositiveIntegerField(help_text='duration of procedure in minutes')
    duration = models.DurationField(help_text='duration of the procedure')
    spec = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='procedures')

    def __str__(self):
        """
        Magic method is redefined to show information about Procedure.
        :return: procedure name
        """
        return str(self.name)

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Procedure object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
