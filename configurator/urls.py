from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='config-home'),
    path('standard/', views.standard_button, name='stand-butt'),
    path('get_contact_type', views.get_contact_type, name='contact-type')
]
