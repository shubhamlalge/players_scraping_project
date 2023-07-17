from rest_framework import viewsets
from .models import Player
from .serializer import PlayerSerializer
from .permissions import CustomPermission


class PlayerViewSet(viewsets.ModelViewSet):
    '''This class is used for perform crud operations for player model'''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [CustomPermission]
