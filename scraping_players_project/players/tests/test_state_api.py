'''This module is used for write test cases for state api'''

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from players.models import State


class StateViewSetAPITestCases(APITestCase):
    '''Test cases for the StateViewSet API'''

    def setUp(self):
        '''this function used to Setup the environment before run the test cases'''

        self.superuser = 'admin'
        self.password = '1111'
        self.user = 'user'
        # Create a superuser
        self.superuser_obj = User.objects.create_superuser(self.superuser, 'admin@example.com', self.password)
        # Create a regular user
        self.user_obj = User.objects.create_user(self.user, 'user@example.com', self.password)
        self.state = State.objects.create(name='MH')
        self.url = '/api/state/'
        self.state_data = {
            'name': 'MH'
        }

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        '''This function used for login user or superuser to particular test'''
        self.client.login(username=username, password=password)

    def test_unauthenticated_user_cannot_get_list(self):
        '''This function used for test a unauthenticated user can't get a list of states'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_list(self):
        '''This function used for test a authenticated user can get a list of states'''
        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_can_get_list(self):
        '''This function used for test superuser can get a list of states'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_state(self):
        '''This function used for test unauthenticated user can't create a new state'''
        response = self.client.post(self.url, self.state_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_create_state(self):
        '''This function used for test authenticated user can't create a new state'''

        self.authenticate_user(self.user, self.password)
        response = self.client.post(self.url, self.state_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_create_state(self):
        '''This function used for test superuser can create a new state'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.post(self.url, self.state_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_get_state_detail(self):
        '''This function used for test unauthenticated user can't get a state by there id '''

        response = self.client.get(self.url, kwargs={'pk': self.state.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_state_detail(self):
        '''This function used for test authenticated user can get a state by there id'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.state.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_can_get_state_detail(self):
        '''This function used for test superuser can get a state by there id'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.state.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_update_state(self):
        '''This function used for test unauthenticated user can't update state'''

        response = self.client.put(reverse('state-detail', kwargs={'pk': self.state.id}), self.state_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_update_state(self):
        '''This function used for test authenticated user can't update state'''

        self.authenticate_user(self.user, self.password)
        response = self.client.put(reverse('state-detail', kwargs={'pk': self.state.id}), self.state_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_update_state(self):
        '''This function used for test superuser can update state'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.put(reverse('state-detail', kwargs={'pk': self.state.id}), self.state_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_partial_update_state(self):
        '''This function used for test unauthenticated user can't partially update state'''

        response = self.client.patch(reverse('state-detail', kwargs={'pk': self.state.id}), self.state_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_partial_update_state(self):
        '''This function used for test authenticated user can't partially update state'''

        self.authenticate_user(self.user, self.password)
        response = self.client.patch(reverse('state-detail', kwargs={'pk': self.state.id}), self.state_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_partial_update_state(self):
        '''This function used for test superuser can partially update state'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.patch(reverse('state-detail', kwargs={'pk': self.state.id}), self.state_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_delete_state(self):
        '''This function used for test unauthenticated user can't delete state'''
        response = self.client.delete(reverse('state-detail', kwargs={'pk': self.state.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_delete_state(self):
        '''This function used for test authenticated user can't delete state'''

        self.authenticate_user(self.user, self.password)
        response = self.client.delete(reverse('state-detail', kwargs={'pk': self.state.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_delete_state(self):
        '''This function used for test superuser can delete state'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.delete(reverse('state-detail', kwargs={'pk': self.state.id}), self.state_data,
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
