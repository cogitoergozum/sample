from django.conf.urls import url

from views import index,  editperson, listpersons
urlpatterns = [
    url(r'^$',index, name='pim-index'),
    url(r'^edit/(?P<person_id>[0-9]+)/$',editperson,name='pim-edit'),
    url(r'^list/$',listpersons,name='pim-list')

]