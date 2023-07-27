'''This module is used for write test cases for player api'''

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from players.models import Player,City,State,Position,Class,School

class PlayerViewSetAPITestCases(APITestCase):
    '''Test cases for the PlayerViewSet API'''

    def setUp(self):
        '''this function used to Setup the environment before run the test cases'''

        self.superuser = 'super'
        self.password = '1111'
        self.user = 'user'
        # Create a superuser
        self.superuser_obj = User.objects.create_superuser(self.superuser, 'admin@example.com', self.password)

        # Create a regular user
        self.user_obj = User.objects.create_user(self.user, 'user@example.com', self.password)
        self.url = '/api/players/'
        self.city = City.objects.create(name='demo city')
        self.player_class = Class.objects.create(name='2022')
        self.school = School.objects.create(name='test school', url='https://demourl')
        self.position = Position.objects.create(name='MD')
        self.state = State.objects.create(name='MH')
        self.player = Player.objects.create(image_url='https://demoimageurl', full_name='test name',
                                            height='6 ft',
                                            weight='200', city=self.city, position=self.position,
                                            state=self.state, clas=self.player_class, school=self.school)
        self.player_data = {
            'position_name': 'test position',
            'class_name': 'test class',
            'state_name': 'test state',
            'city_name': 'test city',
            'school_name': 'test school',
            'school_url' : 'https://demoschoolurl',
            'commitment_school_name' : 'test commitment school name',
            'commitment_url' : 'https://democommitmenturl',
            'recruiters': 'test recruiters',
            'image_url': 'https://demoimageurl',
            'full_name': 'test demo',
            'height': '6 ft',
            'weight': '200'

        }

    # Helper method to authenticate the user
    def authenticate_user(self, username, password):
        '''This function used for login user or superuser to particular test'''

        self.client.login(username=username, password=password)

    def test_unauthenticated_user_cannot_get_list(self):
        '''This function used for test a unauthenticated user can't get a list of players'''

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_list(self):
        '''This function used for test a authenticated user can get a list of players'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_can_get_list(self):
        '''This function used for test superuser can get a list of players'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_player(self):
        '''This function used for test unauthenticated user can't create a new player'''
        response = self.client.post(self.url, self.player_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_create_player(self):
        '''This function used for test authenticated user can't create a new player'''

        self.authenticate_user(self.user, self.password)
        response = self.client.post(self.url, self.player_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_create_player(self):
        '''This function used for test superuser can create a new player'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.post(self.url, self.player_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_get_player_detail(self):
        '''This function used for test unauthenticated user can't get a player by there id '''
        response = self.client.get(self.url, kwargs={'pk': self.player.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_get_player_detail(self):
        '''This function used for test authenticated user can get a player by there id'''

        self.authenticate_user(self.user, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.player.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_user_can_get_player_detail(self):
        '''This function used for test superuser can get a player by there id'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.get(self.url, kwargs={'pk': self.player.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_update_player(self):
        '''This function used for test unauthenticated user can't update player'''
        response = self.client.put(reverse('players-detail', kwargs={'pk': self.player.id}), self.player_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_update_player(self):
        '''This function used for test authenticated user can't update player'''

        self.authenticate_user(self.user, self.password)
        response = self.client.put(reverse('players-detail', kwargs={'pk': self.player.id}), self.player_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_update_player(self):
        '''This function used for test superuser can update player'''
        self.authenticate_user(self.superuser, self.password)
        response = self.client.put(reverse('players-detail', kwargs={'pk': self.player.id}), self.player_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_partial_update_player(self):
        '''This function used for test unauthenticated user can't partially update player'''
        response = self.client.patch(reverse('players-detail', kwargs={'pk': self.player.id}), self.player_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_partial_update_player(self):
        '''This function used for test authenticated user can't partially update player'''

        self.authenticate_user(self.user, self.password)
        response = self.client.patch(reverse('players-detail', kwargs={'pk': self.player.id}), self.player_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_partial_update_player(self):
        '''This function used for test superuser can partially update player'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.patch(reverse('players-detail', kwargs={'pk': self.player.id}), self.player_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_delete_player(self):
        '''This function used for test unauthenticated user can't delete player'''
        response = self.client.delete(reverse('players-detail', kwargs={'pk': self.player.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_cannot_delete_player(self):
        '''This function used for test authenticated user can't delete player'''

        self.authenticate_user(self.user, self.password)
        response = self.client.delete(reverse('players-detail', kwargs={'pk': self.player.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_user_can_delete_player(self):
        '''This function used for test superuser can delete player'''

        self.authenticate_user(self.superuser, self.password)
        response = self.client.delete(reverse('players-detail', kwargs={'pk': self.player.id}), self.player_data,
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
