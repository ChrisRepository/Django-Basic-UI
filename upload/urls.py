from django.conf.urls import patterns, include, url
from upload import views
from django.views.generic import TemplateView
urlpatterns = patterns('',
  url(r"^$", TemplateView.as_view(template_name = "upload/index.html"), name = "upload"),
  url(r'^handledata/$', views.handledata, name='handledata'),
  url(r'^delete/(\d+)/$', views.delete, name='delete'), 
  url(r'^list/$', views.list, name='list'),
)
