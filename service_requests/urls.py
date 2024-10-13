from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('account/', views.view_account, name='view_account'),
    path('manage/', views.manage_requests, name='manage_requests'),
]
