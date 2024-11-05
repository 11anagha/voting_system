from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="election_home"),
    path("candidates/", views.candidates, name="candidates"),
    path("vote/<int:pk>", views.vote, name="vote"),   
    
]