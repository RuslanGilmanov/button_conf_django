from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='config-home'),
    path('standard/', views.standard_button, name='stand-butt'),
    path('get_contact_type', views.get_contact_type, name='contact-type'),
    path('standard/load_contact_types/', views.load_contact_types, name='load_contact_types'),
    path('standard/load_colors/', views.load_colors, name='load_colors'),
    path('standard/load_pressel_legend/', views.load_legends, name='load_pressel_legend')
]
