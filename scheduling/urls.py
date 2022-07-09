from django.urls import path, include, re_path

from .views import ScheduleCreateList, ScheduleDetail, LocationCreateList, LocationDetail, ProcedureCreateList, \
    ProcedureDetail, AppointmentCreateList, AppointmentDetail, SpecialistFreeTimeGET, FreeSpecialists, ListCustomers

app_name = 'scheduling'
urlpatterns = [

    path('schedule/create/', ScheduleCreateList.as_view(), name='schedule_create'),
    path('schedule/<int:pk>/', ScheduleDetail.as_view(), name='schedule_detail'),

    path('location/create/', LocationCreateList.as_view(), name='location_create'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location_detail'),

    path('procedure/create/', ProcedureCreateList.as_view(), name='procedure_create'),
    path('procedure/<int:pk>/', ProcedureDetail.as_view(), name='procedure_detail'),

    path('appointment/create/', AppointmentCreateList.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/', AppointmentDetail.as_view(), name='appointment_detail'),

    path('spec_free_time/', SpecialistFreeTimeGET.as_view(), name='specialist_free_time'),
    path('free_specs/', FreeSpecialists.as_view(), name='free_specialist'),
    path('customers_list/', ListCustomers.as_view(), name='list_customers'),

]
