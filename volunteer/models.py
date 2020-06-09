from django.db import models

# Create your models here.


class IntroduceSpeaker(models.Model):
    full_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    S_fullname = models.CharField(max_length=30, null=True, blank=True)
    S_email = models.EmailField(null=True, blank=True)
    S_reason = models.CharField(max_length=30, null=True, blank=True)
    S_idea = models.CharField(max_length=30, null=True, blank=True)
    number = models.CharField(max_length=30, null=True, blank=True)
    verb = models.CharField(max_length=30, null=True, blank=True)
