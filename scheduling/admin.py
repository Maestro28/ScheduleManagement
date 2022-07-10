from django.contrib import admin

from .models.appointment_model import Appointment
from .models.location_model import Location
from .models.procedure_model import Procedure
from .models.schedule_model import Schedule

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Location)
admin.site.register(Procedure)
admin.site.register(Schedule)
