from rest_framework.routers import DefaultRouter

from .views import SpeakerVolunteer

router = DefaultRouter()

router.register(r'speaker', SpeakerVolunteer, basename='speaker_volunteer')

urlpatterns = router.urls
