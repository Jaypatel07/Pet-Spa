from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^AboutUs$', views.aboutus),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/add$', views.add),
    url(r'^dashboard/addProcess$', views.add_process), 
    url(r'^dashboard/appointment/(?P<id>\d+)$', views.appointment), 
    url(r'^dashboard/edit/(?P<id>\d+)$', views.edit), 
    url(r'^dashboard/profile/(?P<id>\d+)$', views.profile), 
    url(r'^dashboard/processEdit/(?P<id>\d+)$', views.process_edit),
   
]