from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
    This serializer class is used for all fields
    '''

    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    '''
    This serializer class is used for login purpose it contains username and password
    '''

    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=20, allow_blank=False, allow_null=False)

    def validate(self, attrs, user=None):

        email = attrs.get('email')
        password = attrs.get('password')
        username = attrs.get('username')
        if username and email:
            raise serializers.ValidationError('Provide either username or email, not both')
        if not username and not email:
            raise serializers.ValidationError("Provide either username or password")

        if username or email and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                try:
                    user = User.objects.get(email=email)
                    user = authenticate(request=self.context.get('request'), username=user.username, password=password)
                except:
                    raise serializers.ValidationError("Unable to do login provide valid credentials")
        else:
            raise serializers.ValidationError('Must enter email or username and password')
        attrs['user'] = user
        return attrs


class CustomUpdateSerializer(serializers.ModelSerializer):
    '''This serializer class for exclude update fields
    '''

    class Meta:
        model = User

        exclude = ['username', 'email', 'password']
