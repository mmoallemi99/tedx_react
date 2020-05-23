from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import SendMailFromSpeakerSerializer



class SpeakerVolunteer(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = SendMailFromSpeakerSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data='your information is sent to organizer')
