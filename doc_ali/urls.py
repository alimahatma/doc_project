from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('cards/', include('cards.urls')),
  
  

]
