from django.urls import path
from . import views

urlpatterns = [
    path('callback', views.index, name='callback'),
    path('', views.blank, name='blank')
]
