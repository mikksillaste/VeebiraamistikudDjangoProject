from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Lisa endpoint
    url(r'^api/data$', views.get_data, name='api-data'),
]