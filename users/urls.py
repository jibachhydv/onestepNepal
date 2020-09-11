# Importing path module
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    # Login
    path('login/', views.login, name='login'),

    # Logout
    path('logout/', views.logout, name='logout'),

    # Password Change
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),

    # Password Change Done 
    path('password_change_done', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Reset Password
    path('password_reset/',
            views.PasswordResetView.as_view(),
            name='password_reset'),

    path('password_reset_done/',
                views.PasswordResetDoneView.as_view(),
                name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
                views.PasswordResetConfirmView.as_view(),
                name='password_reset_confirm'),

    path('reset/done/',
                views.PasswordResetCompleteView.as_view(),
                name='password_reset_complete'),
]