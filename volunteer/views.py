from django.shortcuts import render

# Create your views here.
import json
import smtplib,ssl
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from django.http import HttpResponse



class SpeakerVolunteer(viewsets.ViewSetMixin, generics.CreateAPIView):
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        port = 465
        password = '123yekdose'
        context = ssl.create_default_context()
        smtp_server = 'smtp.gmail.com'
        sender = "my.ted.testmail@gmail.com"
        reciever = "Tedxuniversityofisfahan1@gmail.com"
        introduce_speaker = """/
        Subject: test for speaker volunteer's
        hi lovely organizer :)
        some one introduce a speaker
        first name: {}
        last name: {}
        email: {}
        phone number: {}
        full name of speaker: {}
        speaker's email: {}
        reason : {}
        idea : {}



        """.format(data.get('firstname'), data.get('lastname'), data.get('email'), data.get('phone number'),
                   data.get('S-full name'), data.get('S-email'), data.get('S-reason'), data.get('S-idea'))
        be_speaker = """

        Subject: test for speaker volunteer's
        hi lovely organizer :)
        some one sends request to be speaker

        full name of speaker: {}
        speaker's email: {}
        speaker's number: {}
        idea : {}


        """.format(data.get('S-full name'), data.get('S-email'), data.get('number'), data.get('S-idea'))
        message = None
        if data.get('verb') == 'introduce':
            message = introduce_speaker
        elif (data.get('verb') == 'be'):
            message = be_speaker
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, reciever, message)
        return HttpResponse(status=200)

