from rest_framework import serializers
from .models import Player, City, Class, Commitment, School, State, Position


class PositionSerializer(serializers.ModelSerializer):
    '''This class is used for serialize position '''

    class Meta:
        model = Position
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    '''This class is used for serialize Class '''

    class Meta:
        model = Class
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    '''This class is used for serialize state '''

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    '''This class is used for serialize city '''

    class Meta:
        model = City
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    '''This class is used for serialize school '''

    class Meta:
        model = School
        fields = '__all__'


class CommitmentSerializer(serializers.ModelSerializer):
    '''This class is used for serialize commitment '''

    school = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Commitment
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    '''This class is used for serialize players'''

    position = serializers.PrimaryKeyRelatedField()
    clas = serializers.PrimaryKeyRelatedField()
    state = serializers.PrimaryKeyRelatedField()
    city = serializers.PrimaryKeyRelatedField()
    school = serializers.PrimaryKeyRelatedField()
    commitment = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Player
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    '''This class is used for serialize offers'''

    schools = serializers.PrimaryKeyRelatedField(many=True)
    player = serializers.PrimaryKeyRelatedField()
