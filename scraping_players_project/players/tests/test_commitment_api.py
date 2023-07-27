'''This module is used for write test cases for commitment api'''

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from players.models import Committment, School


class CommitmentViewSetAPITestCases(APITestCase):
    '''Test cases for the CommitmentViewSet API'''

    def setUp(self):
        '''this function used to Setup the environment before run the test cases'''
        self.school = School.objects.create(name='test school', url='https://demourl')
        self.commitment = Committment.objects.create(school=self.school,
                                                     recruiters='demo recruiters')
        self.password = '1111'
        self.superuser = 'admin'
        self.user = 'user'
        # Create a superuser
        self.superuser_obj = User.objects.create_superuser(self.superuser, 'admin@example.com', self.password)
        # Create a regular user
        self.user_obj = User.objects.create_user(self.user, 'user@example.com', self.password)
        self.url = '/api/commitment/'
        self.commitment_data = {
            'school_name': 'test school',
            'school_url': 'https://demourl',
            'recruiters': 'demo recruiters'
        }

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        '''This function used for login user or superuser to particular test'''
        self.client.login(username=username, password=password)

    def test_unauthenticated_user_cannot_get_list(self):
        '''This function used for test a unauthenticated user can't get a list of Commitments'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_list(self):
        '''This function used for test a authenticated user can get a list of Commitments'''
        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_can_get_list(self):
        '''This function used for test superuser can get a list of Commitments'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_commitment(self):
        '''This function used for test unauthenticated user can't create a new Commitment'''
        response = self.client.post(self.url, self.commitment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_create_commitment(self):
        '''This function used for test authenticated user can't create a new Commitment'''
        self.authenticate_user(self.user, self.password)
        response = self.client.post(self.url, self.commitment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_create_commitment(self):
        '''This function used for test superuser can create a new Commitment'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.post(self.url, self.commitment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_get_commitment_detail(self):
        '''This function used for test unauthenticated user can't get a Commitment by there id '''
        response = self.client.get(self.url, kwargs={'pk': self.commitment.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_commitment_detail(self):
        '''This function used for test authenticated user can get a Commitment by there id'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(reverse('commitment-detail', kwargs={'pk': self.commitment.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_can_get_commitment_detail(self):
        '''This function used for test superuser can get a Commitment by there id'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(reverse('commitment-detail', kwargs={'pk': self.commitment.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_update_commitment(self):
        '''This function used for test unauthenticated user can't update Commitment'''

        response = self.client.put(reverse('commitment-detail', kwargs={'pk': self.commitment.id}),
                                   self.commitment_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_update_commitment(self):
        '''This function used for test authenticated user can't update Commitment'''

        self.authenticate_user(self.user, self.password)
        response = self.client.put(reverse('commitment-detail', kwargs={'pk': self.commitment.id}),
                                   self.commitment_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_update_commitment(self):
        '''This function used for test superuser can update Commitment'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.put(reverse('commitment-detail', kwargs={'pk': self.commitment.id}),
                                   self.commitment_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_partial_update_commitment(self):
        '''This function used for test unauthenticated user can't partially update Commitment'''
        response = self.client.patch(reverse('commitment-detail', kwargs={'pk': self.commitment.id}),
                                     self.commitment_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_partial_update_commitment(self):
        '''This function used for test authenticated user can't partially update Commitment'''
        self.authenticate_user(self.user, self.password)
        response = self.client.patch(reverse('commitment-detail', kwargs={'pk': self.commitment.id}),
                                     self.commitment_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_partial_update_commitment(self):
        '''This function used for test superuser can partially update Commitment'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.patch(reverse('commitment-detail', kwargs={'pk': self.commitment.id}),
                                     self.commitment_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_delete_commitment(self):
        '''This function used for test unauthenticated user can't delete Commitment'''
        response = self.client.delete(reverse('commitment-detail', kwargs={'pk': self.commitment.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_delete_commitment(self):
        '''This function used for test authenticated user can't delete Commitment'''

        self.authenticate_user(self.user, self.password)
        response = self.client.delete(reverse('commitment-detail', kwargs={'pk': self.commitment.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_delete_commitment(self):
        '''This function used for test superuser can delete Commitment'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.delete(reverse('commitment-detail', kwargs={'pk': self.commitment.id}),
                                      self.commitment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
