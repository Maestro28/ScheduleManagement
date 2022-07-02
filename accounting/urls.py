from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from .views import UserDetail, UserByMailDetail, UserCreateList, SpecializationCreateList, SpecializationDetail

# router = routers.DefaultRouter()
# router.register(r'/spec/create/', SpecializationCreateList)

app_name = 'accounting'
urlpatterns = [
    # path('', include(router.urls)),

    path('user/create/', UserCreateList.as_view(), name='user_create'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('user/<str:email>/', UserByMailDetail.as_view(), name='user_detail_mail'),

    path('spec/create/', SpecializationCreateList.as_view(), name='spec_create'),
    path('spec/<int:pk>/', SpecializationDetail.as_view(), name='spec_detail'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]