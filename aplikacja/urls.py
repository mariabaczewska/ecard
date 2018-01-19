from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patient/list/', views.patient_list, name='patient_list'),
    url(r'^patient/([0-9]+)/', views.patient_details, name='patient_details'),
    url(r'^patient/add/', views.patient_add, name='patient_add'),

    url(r'^measurement/add/', views.measurement_add, name='measurement_add'),

#    url(r'^user/list/', views.user_list, name='user_list'),
#    url(r'^user/add/', views.user_add, name='user_add'),
]
