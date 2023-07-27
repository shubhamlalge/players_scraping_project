from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

'''This module is powerful feature that combines the logic for handling API CRUD operations into a single class.'''
from .models import Player, City, Class, School, State, Position, Committment, Offer

'''This module does import all models classes from players models.py '''
from .serializer import PlayerSerializer, ClassSerializer, SchoolSerializer, StateSerializer, PositionSerializer, \
    CommitmentSerializer, OfferSerializer, CitySerializer

'''This module does import all serializer classes from players serializer.py '''
from .permissions import CustomPermission

'''This module does to import '''
from .pagination import CustomPagination


class PlayerViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud operations on player '''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination


class CityViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud opertion on city  '''
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [CustomPermission]


class ClassViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud opertion on Class   '''
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [CustomPermission]


class SchoolViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud opertion on school  '''
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination


class StateViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud opertion on state  '''
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [CustomPermission]


class PositionViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud opertion on position  '''
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [CustomPermission]


class CommitmentViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud opertion on commitment  '''
    queryset = Committment.objects.all()
    serializer_class = CommitmentSerializer
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination


class OfferViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud opertion on offer  '''
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination
