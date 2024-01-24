
from django.urls import path
from . import views

urlpatterns=[
    path('', views.main, name='main'),
    path('service', views.service, name='service'),
    path('doctor', views.doctor, name='doctor'),
    path('client', views.client, name='client'),
    path('contact', views.contact, name='contact'),
]