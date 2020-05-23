from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import SpeakerVolunteer

urlpatterns = [
    path(r'speaker/', SpeakerVolunteer.as_view())
]
