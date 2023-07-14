from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login', views.LoginPage, name='login'),
    path('home', views.HomePage, name='home'),
    path('logout', views.LogoutPage, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='../templates/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='../templates/reset_password_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='../templates/password_reset.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='../templates/password_reset.html'), name="password_reset_complete"),
]
