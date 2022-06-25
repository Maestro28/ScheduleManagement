from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import SpecializationCreateView

app_name = 'accounting'
urlpatterns = [
    path('spec/create/', SpecializationCreateView.as_view(), name='spec_create'),
    path('spec/create_copy/', SpecializationCreateView.as_view(), name='spec_create_copy'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]