from django.urls import path
from .views import UserApi, CrimeMap
from rest_framework.authtoken import views

urlpatterns = [
    path('user/', UserApi.as_view(), name="user-detail"),
    path('login/', views.obtain_auth_token),
    path('crime/', CrimeMap.as_view(), name='crime'),
]