from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import IntroduceSpeakerSerializer


class SpeakerVolunteer(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = IntroduceSpeakerSerializer
