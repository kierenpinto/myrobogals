from django.conf.urls import url
from . import views

app_name = 'rgsupport'
urlpatterns = [
    #url(r'^admin/$', views.get),
    url(r'^query/$', views.get_requestform, name = 'query'),
    url(r'thanks/$',views.get_thanks, name = 'thanks'),
    url(r'^', views.get_requestform),
]