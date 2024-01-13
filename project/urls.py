from django.urls import path
from . import views
urlpatterns = [
    path("", views.ham, name="demo"),
    path("h", views.ab, name="home")
]