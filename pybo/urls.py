from django.urls import path

from .views import *

app_name = 'pybo'
urlpatterns = [
    path('', index, name='index'),
]
