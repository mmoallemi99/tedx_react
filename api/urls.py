from rest_framework import routers

from django.urls import path, include

from .views import (
    # EventViewSet,
    StaffViewSet,
    SpeakerViewSet,
    SponsorViewSet,
    AttendeeCreateAPIView,
)

app_name = 'api'

router = routers.DefaultRouter()
# router.register(r'events', EventViewSet)
router.register(r'staffs', StaffViewSet)
router.register(r'speakers', SpeakerViewSet)
router.register(r'sponsors', SponsorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', AttendeeCreateAPIView.as_view()),

    # path('', EventViewSet.as_view, name='event'),
]
