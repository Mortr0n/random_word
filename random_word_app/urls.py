from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('make_word', views.make_word),
]
