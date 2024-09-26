from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='config-home'),
    path('standard/', views.standard_button, name='stand-butt'),
    path('get_contact_type', views.get_contact_type, name='contact-type'),
    path('standard/load_contact_types/', views.load_contact_types, name='load_contact_types'),
    path('standard/load_colors/', views.load_colors, name='load_colors'),
    path('pressel_selection/load_legend/', views.load_legends, name='load_pressel_legend'),
    path('pressel_selection/load_pressel_finish/', views.load_finish, name='load_pressel_finish'),
    path('pressel_selection/load_polycarbonate_color/', views.load_polycarb_color, name='load_polycarb_color'),
    path('pressel_selection/', views.select_pressel, name='select-pressel'),
    path('m20/', views.m20_button, name='m20-butt')
]
