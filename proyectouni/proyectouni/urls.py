"""proyectouni configuracion URL
"""
from django.urls import path , include


urlpatterns = [
    path('appuni/', include('appuni.urls')),
]