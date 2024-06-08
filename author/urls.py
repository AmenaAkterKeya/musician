from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.resister, name='signup'),
    path('log_in/', views.user_login, name='login'),
    path('log_out/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/pass_change/', views.pass_change, name='pass_change'),
    path('profile/without_pass/', views.without_pass, name='without_pass'),
]