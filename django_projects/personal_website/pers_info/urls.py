from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('travels/', views.travels, name='travels'),
  path('projects/', views.projects, name='projects'),
  path('classes/', views.classes, name='classes'),

]
