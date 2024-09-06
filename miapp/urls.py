from django.urls import path
from .views import hola_mundo

urlpatterns = [
    path('', hola_mundo),  # Ruta para la vista hola_mundo
]
