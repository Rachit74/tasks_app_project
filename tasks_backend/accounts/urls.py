from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("v1/register/", views.RegisterView.as_view(), name='register'),
    path("v1/login/", views.LoginView.as_view(), name='login'),
    path("v1/token/refresh", TokenRefreshView.as_view(), name='token_refresh'),
]