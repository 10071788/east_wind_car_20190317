#from django.urls import path
from django.conf.urls import url, include

from eastcar import views

urlpatterns = [
    url(r'^eastcars/$', views.RentalCar_list),
    url(r'^eastcars/(?P<pk>[0-9]+)/$', views.RentalCar_detail),
]
