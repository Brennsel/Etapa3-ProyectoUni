from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumno/<str:nombre_alumno>/', views.nombre_alumno, name='nombre_alumno'),
    path('nuevo-alumno/', views.nuevo_alumno, name='nuevo_alumno'),
]

#PLUS OPCIONAL:

urlpatterns += [
    path('actualizar-alumno/<int:pk>', views.actualizar_alumno, name='actualizar_alumno'),
    path('eliminar-alumno/<int:pk>', views.eliminar_alumno, name='eliminar_alumno'),
]