from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_home, name="home"),
    path('research/', views.research, name="research"),
]
