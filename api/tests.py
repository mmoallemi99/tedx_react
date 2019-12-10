from rest_framework.test import (
    APIClient,
    APITestCase,
    RequestsClient,
    APILiveServerTestCase,
)
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse

from .utils import test_image_generator
from tedx.events.models import (
    Event,
    Staff,
    Speaker,
    Sponsor,
)

MAX_OBJECTS = 5


class EventViewSetUnitTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.event = Event.objects.create(name='TEDx UI 2019')

    def test_can_retrieve_event(self):
        event = Event.objects.get()
        response = self.client.get(
            api_reverse('api:event-detail', kwargs={
                'pk': event.id,
            }),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, event)


class EventAPIConsumerTest(APILiveServerTestCase):

    def setUp(self):
        self.client = RequestsClient()

        self.event = Event.objects.create(
            name='TEDx 2019',
            year=2019,
        )

        response = self.client.get(self.live_server_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_retrieve_events(self):
        events_url = self.live_server_url + '/events/'
        client = self.client
        response = client.get(events_url)
        valid_event_data = {
            'url': 'http://testserver/events/' + str(self.event.id) + '/',
            'name': self.event.name,
            'year': self.event.year,
            'staff_set': [],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(valid_event_data, response.json())


class StaffViewSetUnitTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.event = Event.objects.create(name='TEDx 2019')
        image = test_image_generator()
        self.staff = Staff.objects.create(
            event=self.event,
            first_name='Mohammad',
            last_name='Moallemi',
            role='programmer',
            picture=image,
        )

    def test_can_retrieve_staff(self):
        staff = Staff.objects.get()
        response = self.client.get(
            api_reverse('api:staff-detail', kwargs={
                'pk': staff.id
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, staff)


class StaffAPIConsumerTest(APILiveServerTestCase):

    def setUp(self):
        self.client = RequestsClient()

        self.event = Event.objects.create(name='TEDx 2019')
        image = test_image_generator()
        for _ in range(MAX_OBJECTS):
            self.staff = Staff.objects.create(
                event=self.event,
                first_name='Mohammad',
                last_name='Moallemi',
                role='programmer',
                picture=image,
            )

        response = self.client.get(self.live_server_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_retrieve_staffs(self):
        staff_url = self.live_server_url + '/staffs/'
        client = self.client
        response = client.get(staff_url)

        image = test_image_generator()
        valid_staff_data = {
            'url': 'http://testserver/staffs/' + str(self.staff.id) + '/',
            'first_name': self.staff.first_name,
            'last_name': self.staff.last_name,
            'event': 'http://testserver/events/' + str(self.staff.event.id) + '/',
            'role': self.staff.role,
            'picture': image,
            'bio': None,
            'linkedin_account': None,
            'github_account': None,
        }

        json_data = response.json()
        self.assertEqual(len(json_data), MAX_OBJECTS)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(valid_staff_data, response.json())


class SpeakerViewSetUnitTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.event = Event.objects.create(name='TEDx 2019')
        image = test_image_generator()
        self.speaker = Speaker.objects.create(
            event=self.event,
            first_name='Masoud',
            last_name='Algooneh',
            email='malg@gmail.com',
            bio='some text',
        )

    def test_can_retrieve_speakers(self):
        speaker = Speaker.objects.get()
        response = self.client.get(
            api_reverse('api:speaker-detail', kwargs={
                'pk': speaker.id,
            }),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(speaker)
        print(response.data)
        self.assertContains(response, speaker)


class SpeakerAPIConsumerTest(APILiveServerTestCase):

    def setUp(self):
        self.client = RequestsClient()

        self.event = Event.objects.create(name='TEDx 2019')
        for _ in range(MAX_OBJECTS):
            self.speaker = Speaker.objects.create(event=self.event)

    def test_api_can_create_sponsor(self):
        speakers_url = self.live_server_url + '/speakers/'
        data = {
            "first_name": "Masoud",
            "last_name": "Algoone",
            "email": "masoudalgoone@gmail.com",
            "phone_number": "09375178053",
            "bio": "Guide Them All",
        }
        response = self.client.post(speakers_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_retrieve_speakers(self):
        speakers_url = self.live_server_url + '/speakers/'
        client = self.client
        response = client.get(speakers_url)
        json_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json_data), MAX_OBJECTS)


class SponsorViewSetUnitTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.event = Event.objects.create(name='TEDx 2019')
        self.sponsor = Sponsor.objects.create(
            event=self.event,
            name='Learnevents',
        )

    def test_can_retrieve_sponsor(self):
        sponsor = Sponsor.objects.get()
        response = self.client.get(
            api_reverse('api:sponsor-detail', kwargs={
                'pk': sponsor.id,
            }),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, sponsor)


class SponsorAPIConsumerTest(APILiveServerTestCase):

    def setUp(self):
        self.client = RequestsClient()

        self.event = Event.objects.create(name='TEDx 2019')
        for _ in range(MAX_OBJECTS):
            self.sponsor = Sponsor.objects.create(event=self.event)

    def test_api_can_retrieve_sponsors(self):
        sponsors_url = self.live_server_url + '/sponsors/'
        client = self.client
        response = client.get(sponsors_url)
        json_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json_data), MAX_OBJECTS)
