from .views import registrar
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "core"

urlpatterns = [
    path('registro/', registrar, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]