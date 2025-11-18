# Ao criar páginas, precisamos configurar a URL, a VIEW e o Template. 

from django.urls import path, include
from .views import homepage

urlpatterns = [
    
    path('', homepage),
]