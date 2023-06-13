from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserProfile

class UserProfileTests(APITestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(name='superU', email='superU@example.com', bio='Some bio')

    def test_create_profile(self):
        url = reverse('user-profile')
        data = {'name': 'superr', 'email': 'superr@example.com', 'bio': 'Some bio'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)  
        self.assertEqual(UserProfile.objects.latest('id').name, 'superr')

    def test_update_profile(self):
        url = reverse('user-profile')
        data = {'name': 'superU'}
        self.client.force



