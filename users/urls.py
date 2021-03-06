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
            auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',
            auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


    # User Registration
    path('signup/', views.signup, name='signup'),

    # User Activation
    path('active/<uidb64>/<token>/', views.activate, name='activate'),

    # Profile 
    path('profile/<str:username>-<int:id>/', views.profile, name='profile')
]