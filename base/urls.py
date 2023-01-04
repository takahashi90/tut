from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name="home"), # it is really convinient to name our urls
    path('room/',views.room, name="room"),
    ]