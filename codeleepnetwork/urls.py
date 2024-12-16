from django.urls import path
from . import views

urlpatterns = [
    path("", views.careers),
    path("<int:id>/", views.careersArgs)
]