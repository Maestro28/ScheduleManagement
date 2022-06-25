from django.urls import path

from .views import SpecializationCreateView

app_name = 'accounting'
urlpatterns = [
    path('spec/create/', SpecializationCreateView.as_view())
]