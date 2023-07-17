from rest_framework import serializers
from .models import Player, City, Class, Commitment, School, State, Position


class PositionSerializer(serializers.ModelSerializer):
    '''This class is used for serialize position data'''

    class Meta:
        model = Position
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    '''This class is used for serialize Class data'''

    class Meta:
        model = Class
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    '''This class is used for serialize state data'''

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    '''This class is used for serialize city data'''

    class Meta:
        model = City
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    '''This class is used for serialize school data'''

    class Meta:
        model = School
        fields = '__all__'


class CommitmentSerializer(serializers.ModelSerializer):
    '''This class is used for serialize commitment data'''

    school = SchoolSerializer()

    class Meta:
        model = Commitment
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    clas = ClassSerializer()
    state = StateSerializer()
    city = CitySerializer()
    school = SchoolSerializer()
    commitment = CommitmentSerializer()

    class Meta:
        model = Player
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    schools = SchoolSerializer(many=True)
    player = PlayerSerializer()
