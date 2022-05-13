from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'cal'
urlpatterns = [
    path('', views.index, name='index'),
    path('group_managing/', views.group_making, name='group_making'),

]
