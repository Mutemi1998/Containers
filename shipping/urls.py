from django.urls import path

from . import views

urlpatterns = [
    # ex: /homepage/
    path('', views.index, name='index'),
]