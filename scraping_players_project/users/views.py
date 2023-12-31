from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer, CustomUpdateSerializer
from .pagination import CustomPagination
from rest_framework.authtoken.views import Token
from rest_framework.response import Response
from django.contrib.auth import login, logout
from users.models import User


class CreateUser(CreateAPIView):
    '''This class is used for user creation'''

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        '''This method is used for convert password into hash password'''
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ListUser(ListAPIView):
    '''This class is used for list user info'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        '''This function is used to give access to view data only authenticated user and superuser give all access'''

        if self.request.user.is_superuser:
            return User.objects.all()
        elif self.request.user.is_authenticated:
            return User.objects.filter(id=self.request.user.id)
        else:
            return User.objects.none()


class RetrieveUpdate(RetrieveUpdateAPIView):
    '''This is a class for update  a data'''

    '''This is a class for updating data'''

    serializer_class = CustomUpdateSerializer
    queryset = User.objects.all()


class RetrieveDelete(RetrieveDestroyAPIView):
    '''This is a class for  delete a data '''

    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(APIView):
    '''This class is used to log in purpose '''

    def post(self, request):
        """
        This function is post request for login a user by taking username and password
        """

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'id': user.id})
        else:
            return Response({'error': 'Invalid credentials'}, status=200)


class Logout(APIView):
    '''This class is used to log out purpose'''

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            token = Token.objects.filter(user=user)
            token.delete()
            logout(request)
            return Response({'message': 'Logged out'})
        else:
            return Response({'error': 'User is not authenticated'}, status=400)
