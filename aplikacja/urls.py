from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.patients_list, name='patients_list'),
    url(r'^patient/([0-9]+)/', views.patient_details, name='patient_details'),
]
