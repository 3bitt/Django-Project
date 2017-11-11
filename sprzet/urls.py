from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^set_detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^set_detail/(?P<pk>[0-9]+)/edit/$', views.set_detail_edit, name='set_detail_edit'),
    url(r'^about/$', views.about, name='about'),


    url(r'^Set/$', views.dodaj_set, name='dodaj_set'),
    url(r'^sprzet/latawiec/$', views.dodaj_latawiec, name='dodaj_latawiec'),
    url(r'^sprzet/deska/$', views.dodaj_deske, name='dodaj_deske'),
    url(r'^sprzet/trapez/$', views.dodaj_trapez, name='dodaj_trapez'),

    url(r'lista_set/$', views.set_list, name='set_list'),
    url(r'^sprzet_list/$', views.sprzet_list, name='sprzet_list'),


    url(r'^sprzet_list/(?P<ident>[A-Z][a-z]+)/(?P<numer>[0-9]+)/$', views.sprzet_detail, name='sprzet_detail'),
    url(r'^sprzet_list/(?P<ident>[A-Z][a-z]+)/(?P<numer>[0-9]+)/edit/$', views.sprzet_detail_edit, name='sprzet_detail_edit'),
    url(r'^sprzet_list/(?P<ident>[A-Z][a-z]+)/(?P<numer>[0-9]+)/usun/$', views.usun_objekt, name='usun_objekt'),
    url(r'^sprzet_list/(?P<ident>[A-Z][a-z]+)/(?P<numer>[0-9]+)/usun/potwierdz/$', views.are_you_sure, name='are_you_sure'),


    
]
