from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('stores/', views.stores, name='stores'),
    path('warranty/', views.warranty, name='warranty'),
    path('contacts/', views.contact, name='contacts'),
]