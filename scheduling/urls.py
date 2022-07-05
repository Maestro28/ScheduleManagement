from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from .views import ScheduleCreateList, ScheduleDetail, LocationCreateList, LocationDetail, ProcedureCreateList, \
    ProcedureDetail, AppointmentCreateList, AppointmentDetail

# router = routers.DefaultRouter()
# router.register(r'/spec/create/', SpecializationCreateList)

app_name = 'scheduling'
urlpatterns = [
    # path('', include(router.urls)),

    path('schedule/create/', ScheduleCreateList.as_view(), name='schedule_create'),
    path('schedule/<int:pk>/', ScheduleDetail.as_view(), name='schedule_detail'),

    path('location/create/', LocationCreateList.as_view(), name='location_create'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location_detail'),

    path('procedure/create/', ProcedureCreateList.as_view(), name='procedure_create'),
    path('procedure/<int:pk>/', ProcedureDetail.as_view(), name='procedure_detail'),

    path('appointment/create/', AppointmentCreateList.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/', AppointmentDetail.as_view(), name='appointment_detail'),

]