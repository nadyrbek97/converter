from django.test import TestCase, Client
from django.urls import reverse


class YoutubeTest(TestCase):

    def setUp(self):
        self.test_link = "https://www.youtube.com/watch?v=NMgLQ950dtg"
        self.client = Client()
        self.home_url = reverse('home-view')

    def test_home_view_post(self):

        response = self.client.post(self.home_url, {'link': self.test_link})

        # testing url redirection code (302)
        self.assertEqual(response.status_code, 302)

    def test_home_view_get(self):

        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)

