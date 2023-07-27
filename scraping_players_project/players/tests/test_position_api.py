'''This module is used for write test cases for position api'''

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from players.models import Position


class PositionViewSetAPITestCases(APITestCase):
    '''Test cases for the PositionViewSet API'''

    def setUp(self):
        '''this function used to Setup the environment before run the test cases'''

        self.superuser = 'admin'
        self.password = '1111'
        self.position = Position.objects.create(name='MD')
        # Create a superuser
        self.superuser_obj = User.objects.create_superuser(self.superuser, 'admin@example.com', self.password)
        self.user = 'user'
        # Create a regular user
        self.user_obj = User.objects.create_user(self.user, 'user@example.com', self.password)
        self.url = '/api/position/'
        self.position_data = {
            'name': 'CF'
        }

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        '''This function used for login user or superuser to particular test'''
        self.client.login(username=username, password=password)

    def test_unauthenticated_user_list(self):
        '''This function used for test a unauthenticated user can't get a list of positions'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_list(self):
        '''This function used for test a authenticated user can get a list of positions'''
        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_list(self):
        '''This function used for test superuser can get a list of positions'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_create(self):
        '''This function used for test unauthenticated user can't create a new position'''
        response = self.client.post(self.url, self.position_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_create(self):
        '''This function used for test authenticated user can't create a new position'''

        self.authenticate_user(self.user, self.password)
        response = self.client.post(self.url, self.position_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_create(self):
        '''This function used for test superuser can create a new position'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.post(self.url, self.position_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_detail(self):
        '''This function used for test unauthenticated user can't get a position by there id '''
        response = self.client.get(self.url, kwargs={'pk': self.position.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_detail(self):
        '''This function used for test authenticated user can get a position by there id'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.position.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_detail(self):
        '''This function used for test superuser can get a position by there id'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.position.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_update(self):
        '''This function used for test unauthenticated user can't update position'''
        response = self.client.put(reverse('position-detail', kwargs={'pk': self.position.id}), self.position_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_update(self):
        '''This function used for test authenticated user can't update position'''

        self.authenticate_user(self.user, self.password)
        response = self.client.put(reverse('position-detail', kwargs={'pk': self.position.id}), self.position_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_update(self):
        '''This function used for test superuser can update position'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.put(reverse('position-detail', kwargs={'pk': self.position.id}), self.position_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_partial_update(self):
        '''This function used for test unauthenticated user can't partially update position'''
        response = self.client.patch(reverse('position-detail', kwargs={'pk': self.position.id}), self.position_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_partial_update(self):
        '''This function used for test authenticated user can't partially update position'''

        self.authenticate_user(self.user, self.password)
        response = self.client.patch(reverse('position-detail', kwargs={'pk': self.position.id}), self.position_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_partial_update(self):
        '''This function used for test superuser can partially update position'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.patch(reverse('position-detail', kwargs={'pk': self.position.id}), self.position_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_delete(self):
        '''This function used for test unauthenticated user can't delete position'''
        response = self.client.delete(reverse('position-detail', kwargs={'pk': self.position.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_delete(self):
        '''This function used for test authenticated user can't delete position'''
        self.authenticate_user(self.user, self.password)
        response = self.client.delete(reverse('position-detail', kwargs={'pk': self.position.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_delete(self):
        '''This function used for test superuser can delete position'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.delete(reverse('position-detail', kwargs={'pk': self.position.id}), self.position_data,
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
