from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.dashboard_with_pivot, name='dashboard_wirh_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
]