from django.urls import path

from . import views

urlpatterns = [
    path('api/create_event/', views.create_event, name='create_event'),
]
