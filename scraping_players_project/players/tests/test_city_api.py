'''This module is used for write test cases for city api'''

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from players.models import City


class CityViewSetAPITestCases(APITestCase):
    '''Test cases for the CityViewSet API'''

    def setUp(self):
        '''this function used to Setup the environment before run the test cases'''

        self.password = '1111'
        self.superuser = 'super'
        self.user = 'user'
        # Create a superuser
        self.superuser = User.objects.create_superuser(self.superuser, 'super@example.com', self.password)
        self.city = City.objects.create(name='demo city')
        # Create a regular user
        self.user = User.objects.create_user(self.user, 'user@example.com', self.password)
        self.url = '/api/city/'
        self.city_data = {
            'name': 'demo city'
        }

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        '''This function used for login user or superuser to particular test'''

        self.client.login(username=username, password=password)

    def test_unauthenticated_user_cannot_get_list(self):
        '''This function used for test a unauthenticated user can't get a list of city list'''

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_list(self):
        '''This function used for test a authenticated user can get a list of city list'''

        self.authenticate_user('user', self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_can_get_list(self):
        '''This function used for test superuser can get a list of city list'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_city(self):
        '''This function used for test unauthenticated user can't create a new city'''

        response = self.client.post(self.url, self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_create_city(self):
        '''This function used for test authenticated user can't create a new city'''

        self.authenticate_user(self.user, self.password)

        response = self.client.post(self.url, self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_create_city(self):
        '''This function used for test superuser can create a new city'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.post(reverse('city-detail', kwargs={'pk': self.city.id}), self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_get_city_detail(self):
        '''This function used for test unauthenticated user can't get a city by there id '''

        response = self.client.get(self.url, kwargs={'pk': self.city.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_city_detail(self):
        '''This function used for test authenticated user can get a city by there id'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.city.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_can_get_city_detail(self):
        '''This function used for test superuser can get a city by there id'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.city.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_update_city(self):
        '''This function used for test unauthenticated user can't update city'''

        response = self.client.put(reverse('city-detail', kwargs={'pk': self.city.id}), self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_update_city(self):
        '''This function used for test authenticated user can't update city'''

        self.authenticate_user(self.user, self.password)
        response = self.client.put(reverse('city-detail', kwargs={'pk': self.city.id}), self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_update_city(self):
        '''This function used for test superuser can update city'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.put(reverse('city-detail', kwargs={'pk': self.city.id}), self.city_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_partial_update_city(self):
        '''This function used for test unauthenticated user can't partially update city'''

        response = self.client.patch(reverse('city-detail', kwargs={'pk': self.city.id}), self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_partial_update_city(self):
        '''This function used for test authenticated user can't partially update city'''

        self.authenticate_user(self.user, self.password)
        response = self.client.patch(reverse('city-detail', kwargs={'pk': self.city.id}), self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_partial_update_city(self):
        '''This function used for test superuser can partially update city'''

        self.authenticate_user(self.superuser, self.password)

        response = self.client.patch(reverse('city-detail', kwargs={'pk': self.city.id}), self.city_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_delete_city(self):
        '''This function used for test unauthenticated user can't delete city'''

        response = self.client.delete(reverse('city-detail', kwargs={'pk': self.city.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_delete_city(self):
        '''This function used for test authenticated user can't delete city'''

        self.authenticate_user(self.user, self.password)
        response = self.client.delete(reverse('city-detail', kwargs={'pk': self.city.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_delete_city(self):
        '''This function used for test superuser can delete city'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.delete(reverse('city-detail', kwargs={'pk': self.city.id}),
                                      format='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
