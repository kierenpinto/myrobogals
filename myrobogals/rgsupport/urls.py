from django.conf.urls import url
from . import views

app_name = 'rgsupport'
urlpatterns = [
    url(r'^admin/message/(?P<pk>[0-9]+)/$',views.IssueDetail.as_view(), name = 'admin_view' ),
    url(r'^admin/message/(?P<pk>[0-9]+)/edit/$', views.get_editform, name='admin_edit'),
    url(r'^admin/message/(?P<pk>[0-9]+)/edit/resolve/$', views.set_resolved, name='admin_resolve'),
    url(r'^admin/home/$',views.IssuesList.as_view(), name = 'admin_list' ),
    url(r'^query/$', views.get_requestform, name = 'query'),
    url(r'thanks/$',views.get_thanks, name = 'thanks'),
    url(r'^', views.get_homeview, name = 'home'),
]