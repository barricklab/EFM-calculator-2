from django.conf.urls import url

from efm2 import views

app_name = 'efm2'
urlpatterns = [
    url(r'^', views.get_sequence, name='index'),
]
