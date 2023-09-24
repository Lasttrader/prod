from django.urls import path

from . import views

app_name = 'firstmlapp'

urlpatterns = [ path('index/', views.index, name= 'index')]