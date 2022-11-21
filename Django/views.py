from week10project import views
from django.urls import path

urlpatterns = [
    path("", views.home),
    path("ccu411315019", views.ccu411315019_function)
]
