from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/calc/', views.calc, name='create_event'),
]
