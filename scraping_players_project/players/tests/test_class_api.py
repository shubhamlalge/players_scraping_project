'''This module is used for write test cases for class api'''

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from players.models import Class


class ClassViewSetAPITestCases(APITestCase):
    '''Test cases for the ClassViewSet API'''

    def setUp(self):
        '''this function used to Setup the environment before run the test cases'''

        # Create a superuser
        self.client = APIClient()
        self.password = '1111'
        self.superuser = 'admin'
        self.player_class = Class.objects.create(name='2022')
        self.superuser_obj = User.objects.create_superuser(self.superuser, 'admin@example.com', self.password)
        self.user = 'user'
        # Create a regular user
        self.user_obj = User.objects.create_user(self.user, 'user@example.com', self.password)
        self.url = '/api/class/'
        self.class_data = {
            'name': '2020'
        }

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        '''This function used for login user or superuser to particular test'''

        self.client.login(username=username, password=password)

    def test_unauthenticated_user_cannot_get_list(self):
        '''This function used for test a unauthenticated user can't get a list of class list'''

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_list(self):
        '''This function used for test a authenticated user can get a list of class list'''
        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_can_get_list(self):
        '''This function used for test superuser can get a list of class list'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_class(self):
        '''This function used for test unauthenticated user can't create a new class'''
        response = self.client.post(self.url, self.class_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_create_class(self):
        '''This function used for test authenticated user can't create a new class'''
        self.authenticate_user(self.user, self.password)

        response = self.client.post(self.url, self.class_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_create_class(self):
        '''This function used for test superuser can create a new class'''
        self.authenticate_user(self.superuser, self.password)

        response = self.client.post(self.url, self.class_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_get_class_detail(self):
        '''This function used for test unauthenticated user can't get a class by there id '''

        response = self.client.get(self.url, kwargs={'pk': self.player_class.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_class_detail(self):
        '''This function used for test authenticated user can get a class by there id'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.player_class.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_can_get_class_detail(self):
        '''This function used for test superuser can get a class by there id'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.player_class.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_update_class(self):
        '''This function used for test unauthenticated user can't update class'''

        response = self.client.put(reverse('class-detail', kwargs={'pk': self.player_class.id}), self.class_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_update_class(self):
        '''This function used for test authenticated user can't update class'''
        self.authenticate_user(self.user, self.password)
        response = self.client.put(reverse('class-detail', kwargs={'pk': self.player_class.id}), self.class_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_update_class(self):
        '''This function used for test superuser can update class'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.put(reverse('class-detail', kwargs={'pk': self.player_class.id}), self.class_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_partial_update_class(self):
        '''This function used for test unauthenticated user can't partially update class'''

        response = self.client.patch(reverse('class-detail', kwargs={'pk': self.player_class.id}), self.class_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_partial_update_class(self):
        '''This function used for test authenticated user can't partially update class'''

        self.authenticate_user(self.user, self.password)
        response = self.client.patch(reverse('class-detail', kwargs={'pk': self.player_class.id}), self.class_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_partial_update_class(self):
        '''This function used for test superuser can partially update class'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.patch(reverse('class-detail', kwargs={'pk': self.player_class.id}), self.class_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_delete_class(self):
        '''This function used for test unauthenticated user can't  delete class'''
        response = self.client.delete(reverse('class-detail', kwargs={'pk': self.player_class.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_delete_class(self):
        '''This function used for test authenticated user can't delete class'''
        self.authenticate_user(self.user, self.password)
        response = self.client.delete(reverse('class-detail', kwargs={'pk': self.player_class.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_delete_class(self):
        '''This function used for test superuser can delete class'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.delete(reverse('class-detail', kwargs={'pk': self.player_class.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
