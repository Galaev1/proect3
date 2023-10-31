
from django.urls import path

from skystore.views import home, contacts, index

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('index/', index),
]