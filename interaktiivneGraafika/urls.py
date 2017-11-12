from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Lisa andmete endpoint
    url(r'^api/data$', views.get_data, name='api-data'),
    # Lisa hääle lisamiseks url endpoint
    url(r'^(?P<inimese_id>[0-9]+)/haaleta/$', views.h22leta, name='haaleta'),

]