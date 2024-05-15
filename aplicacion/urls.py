from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('ver_cursos/', views.ver_cursos, name='ver_cursos'),
    path('crear_cursos/', views.crear_cursos, name='crear_cursos'),
    path('detalles_cursos/<int:id>', views.detalles_cursos, name='detalles_cursos'),
    path('eliminar_cursos/<int:id>', views.eliminar_cursos, name='eliminar_cursos'),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("inicio_sesion/", views.inicio_sesion, name="inicio_sesion"),
]