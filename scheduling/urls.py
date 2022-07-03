from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from .views import ScheduleCreateList

# router = routers.DefaultRouter()
# router.register(r'/spec/create/', SpecializationCreateList)

app_name = 'scheduling'
urlpatterns = [
    # path('', include(router.urls)),

    path('schedule/create/', ScheduleCreateList.as_view(), name='schedule_create'),

]