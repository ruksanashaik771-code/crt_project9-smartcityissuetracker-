from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'report/',
        views.report_issue,
        name='report'
    ),

    path(
        'myissues/',
        views.my_issues,
        name='my_issues'
    ),
path(
    'notifications/',
    views.notifications,
    name='notifications'
),
]