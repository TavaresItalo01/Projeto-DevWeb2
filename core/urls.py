from .views import registrar
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserUpdateView

app_name = "core"

urlpatterns = [
    path('registro/', registrar, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    
    path('editar-perfil/', UserUpdateView.as_view(), name='editar_perfil'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]