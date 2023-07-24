from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Player, City, Class, School, State, Position, Committment, Offer


class ViewsetAPITestCase(APITestCase):
    def setUp(self):
        # Create a superuser
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'password')

        # Create a regular user
        self.user = User.objects.create_user('user', 'user@example.com', 'password')

        # URL for each viewset
        self.urls = {
            'players': '/api/players/',
            'cities': '/api/city/',
            'classes': '/api/class/',
            'schools': '/api/school/',
            'states': '/api/state/',
            'positions': '/api/position/',
            'commitments': '/api/commitment/',
            'offers': '/api/offer/',
        }

        # Add any additional setup for your models here

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        self.client.login(username=username, password=password)

    # Test for unauthorized access (unauthenticated user)
    def test_unauthenticated_user_access(self):
        for url in self.urls.values():
            # Clear any authentication (ensure user is unauthenticated)
            self.client.force_authenticate(user=None)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test for authenticated user with permission (e.g., staff user)
    def test_authenticated_user_with_permission_access(self):
        # Make the regular user a staff user (with appropriate permissions)
        self.user.is_staff = True
        self.user.save()

        for url in self.urls.values():
            self.authenticate_user('user', 'password')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test for superuser access
    def test_superuser_access(self):
        for url in self.urls.values():
            self.authenticate_user('admin', 'password')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
