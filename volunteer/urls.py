from rest_framework.routers import DefaultRouter
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import SpeakerVolunteer

urlpatterns = [
    path(r'speaker/', csrf_exempt(SpeakerVolunteer.as_view()))
]
