from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse


class PositionViewSetAPITestCases(APITestCase):

    def setUp(self):
        # Create a superuser
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'password')

        # Create a regular user
        self.user = User.objects.create_user('user', 'user@example.com', 'password')
        self.url = '/api/position/'

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        self.client.login(username=username, password=password)

    def test_unauthenticated_user_list(self):
        self.client.force_authenticate(user=None)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_list(self):
        self.user.is_active = True
        self.user.save()
        self.authenticate_user('user', 'password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_list(self):
        self.authenticate_user('admin', 'password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_create(self):
        self.client.force_authenticate(user=None)

        data = {
            'name': 'CF'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_create(self):
        self.user.is_active = True
        self.user.save()
        self.authenticate_user('user', 'password')
        data = {
            'name': 'CF'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_superuser_user_create(self):
        self.authenticate_user('admin', 'password')
        data = {
            'name': 'CF'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_detail(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url, kwargs={'pk': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_detail(self):
        self.user.is_active = True
        self.user.save()
        self.authenticate_user('user', 'password')
        response = self.client.get(self.url, kwargs={'pk': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_detail(self):
        self.authenticate_user('admin', 'password')
        response = self.client.get(self.url, kwargs={'pk': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_update(self):
        data = {
            'name': 'CF'
        }

        self.client.force_authenticate(user=None)
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_update(self):
        data = {
            'name': 'CF'
        }
        self.user.is_active = True
        self.user.save()
        self.authenticate_user('user', 'password')
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_superuser_user_update(self):
        data = {
            'name': 'CF'
        }
        self.authenticate_user('admin', 'password')
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_partial_update(self):
        data = {
            'name': 'CF'
        }

        self.client.force_authenticate(user=None)
        response = self.client.patch(reverse(self.url, kwargs={'pk': self.user.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_partial_update(self):
        data = {
            'name': 'CF'
        }
        self.user.is_active = True
        self.user.save()
        self.authenticate_user('user', 'password')
        response = self.client.patch(reverse(self.url, kwargs={'pk': self.user.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_superuser_user_partial_update(self):
        data = {
            'name': 'CF'
        }
        self.authenticate_user('admin', 'password')
        response = self.client.patch(reverse(self.url, kwargs={'pk': self.user.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_delete(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url, kwargs={'pk': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_delete(self):
        self.user.is_active = True
        self.user.save()
        self.authenticate_user('user', 'password')
        response = self.client.delete(reverse(self.url, kwargs={'pk': self.user.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_superuser_user_delete(self):
        self.authenticate_user('admin', 'password')
        response = self.client.delete(reverse(self.url, kwargs={'pk': self.user.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

