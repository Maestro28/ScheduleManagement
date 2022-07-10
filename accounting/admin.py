from django.contrib import admin
from .models.user_model import CustomUser
from .models.specialization_model import Specialization

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Specialization)
