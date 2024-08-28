from django.urls import path
from BlogClase_api.apps.blogs import views

urlpatterns = [
    path('', views.index)
]