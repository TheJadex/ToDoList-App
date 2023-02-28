from django.urls import path
from . import views

# Naming application to make linking between different views/apps easier and to eliminate namespace collisions.
app_name = "tasks"

urlpatterns = [
    # name = "name" --> here, i am giving the views funtion a name
    path("home/", views.name, name="name"),
]