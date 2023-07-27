'''This module is used for write test cases for school api'''

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from players.models import School


class SchoolViewSetAPITestCases(APITestCase):
    '''Test cases for the SchoolViewSet API'''

    def setUp(self):
        '''this function used to Setup the environment before run the test cases'''

        self.superuser = 'admin'
        self.password = '1111'
        self.school = School.objects.create(name='test_school', url='https://demourl')
        # Create a superuser
        self.superuser_obj = User.objects.create_superuser(self.superuser, 'admin@example.com', self.password)
        self.user = 'user'
        # Create a regular user
        self.user_obj = User.objects.create_user(self.user, 'user@example.com', self.password)
        self.url = '/api/school/'
        self.school_data = {
            'name': 'test_school',
            'url': 'https://demourl'
        }

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        '''This function used for login user or superuser to particular test'''
        self.client.login(username=username, password=password)

    def test_unauthenticated_user_list(self):
        '''This function used for test a unauthenticated user can't get a list of schools'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_list(self):
        '''This function used for test a authenticated user can get a list of schools'''
        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_list(self):
        '''This function used for test superuser can get a list of schools'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_create(self):
        '''This function used for test unauthenticated user can't create a new school'''
        response = self.client.post(reverse('school-detail', kwargs={'pk': self.school.id}),
                                    self.school_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_create(self):
        '''This function used for test authenticated user can't create a new school'''

        self.authenticate_user(self.user, self.password)
        response = self.client.post(reverse('school-detail', kwargs={'pk': self.school.id}),
                                    self.school_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_create(self):
        '''This function used for test superuser can create a new school'''

        self.authenticate_user(self.superuser, self.password)

        response = self.client.post(reverse('school-detail', kwargs={'pk': self.school.id}),
                                    self.school_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_detail(self):
        '''This function used for test unauthenticated user can't get a school by there id '''
        response = self.client.get(self.url, kwargs={'pk': self.school.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_detail(self):
        '''This function used for test authenticated user can get a school by there id'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(reverse('school-detail', kwargs={'pk': self.school.id}),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_detail(self):
        '''This function used for test superuser can get a school by there id'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(reverse('school-detail', kwargs={'pk': self.school.id}),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_update(self):
        '''This function used for test unauthenticated user can't update school'''
        response = self.client.put(reverse('school-detail', kwargs={'pk': self.school.id}), self.school_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_update(self):
        '''This function used for test authenticated user can't update school'''

        self.authenticate_user(self.user, self.password)
        response = self.client.put(reverse('school-detail', kwargs={'pk': self.school.id}), self.school_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_update(self):
        '''This function used for test superuser can update school'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.put(reverse('school-detail', kwargs={'pk': self.school.id}), self.school_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_partial_update(self):
        '''This function used for test unauthenticated user can't partially update school'''
        response = self.client.patch(reverse('school-detail', kwargs={'pk': self.school.id}), self.school_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_partial_update(self):
        '''This function used for test authenticated user can't partially update school'''

        self.authenticate_user(self.user, self.password)
        response = self.client.patch(reverse('school-detail', kwargs={'pk': self.school.id}), self.school_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_partial_update(self):
        '''This function used for test superuser can partially update school'''

        self.authenticate_user(self.superuser, self.password)

        response = self.client.patch(reverse('school-detail', kwargs={'pk': self.school.id}), self.school_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_delete(self):
        '''This function used for test unauthenticated user can't delete school'''
        response = self.client.delete(reverse('school-detail', kwargs={'pk': self.school.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_delete(self):
        '''This function used for test authenticated user can't delete school'''

        self.authenticate_user(self.user, self.password)
        response = self.client.delete(reverse('school-detail', kwargs={'pk': self.school.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_delete(self):
        '''This function used for test superuser can delete school'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.delete(reverse('school-detail', kwargs={'pk': self.school.id}), self.school_data,
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
