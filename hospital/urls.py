from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.auth, name='auth'),
    url(r'^auth', views.auth, name='auth'),
    url(r'^add', views.add_prescription, name='add_prescription'),
    url(r'^get', views.get_prescription, name='get_prescription'),
]
