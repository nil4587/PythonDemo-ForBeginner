from django.urls import path
from . import views  # here '.' means the current module

# /products : called root
# /products/1/details
# /products/new

urlpatterns = [
    path("", views.index),
    path("new", views.newproduct)
]
