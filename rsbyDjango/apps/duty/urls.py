
from django.conf.urls import url

from . import views

app_name = 'duty'
urlpatterns = [
    url(r'^list/$', views.DutyListView.as_view(), name='list'),
    url(r'^schedule/$',views.UserListView.as_view(),name='schedule')

]