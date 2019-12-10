from rest_framework import viewsets, generics, permissions

from events.serializers import (
    # EventSerializer,
    StaffSerializer,
    SpeakerSerializer,
    SponsorSerializer,
    AttendeeSerializer,
)
from events.models import (
    # Event,
    Staff,
    Speaker,
    Sponsor,
    Attendee,
)


# class EventViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer


class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class SpeakerViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        request = self.request
        qs = Speaker.objects.all()
        query = request.GET.get('status')
        if query is not None:
            qs = qs.filter(account_status__exact=query)
        return qs

    def perform_update(self, serializer):
        raise PermissionError("You Don't Have Enough Permissions To Update This Instance")

    def perform_destroy(self, instance):
        raise PermissionError("You Don't Have Enough Permissions To Delete This Instance")


class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class AttendeeCreateAPIView(generics.CreateAPIView):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [permissions.AllowAny, ]
