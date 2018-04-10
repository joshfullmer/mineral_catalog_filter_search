from django.conf.urls import url

from . import views

app_name = 'minerals'  # This line is now required for Django 2.0
urlpatterns = [
    url(r'^$', views.mineral_list, name='mineral_list'),
    url(r'random/', views.random_mineral, name='random_mineral'),
    url(r'starting_with/(?P<letter>[A-Za-z])/$',
        views.mineral_letter,
        name='mineral_letter'),
    url(r'by_group/(?P<group>[\w ]+)/$',
        views.mineral_group,
        name='mineral_group'),
    url(r'by_specific_gravity/(?P<specific_gravity>.+)/$',
        views.mineral_specific_gravity,
        name='mineral_specific_gravity'),
    url(r'search/', views.mineral_search, name='mineral_search'),
    url(r'(?P<mineral_id>\d+)/$', views.mineral_detail, name='mineral_detail'),
]
