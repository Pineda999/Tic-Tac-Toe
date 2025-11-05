
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Partida.as_view(), name='juego'),
    path('reiniciar/', views.reiniciar, name='reiniciar'),
]
