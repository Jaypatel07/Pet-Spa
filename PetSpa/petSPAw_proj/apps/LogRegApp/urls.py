from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^welcome$', views.index),
    url(r'^processregistration$', views.processingReg),
    url(r'^processlogin$', views.processingLog),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]
