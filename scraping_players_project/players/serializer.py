from rest_framework import serializers
from .models import Player, City, Class, Committed, School, State, Position


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

    school = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Committed
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    '''This class is used for serialize players'''

    position = serializers.PrimaryKeyRelatedField(read_only=True)
    clas = serializers.PrimaryKeyRelatedField(read_only=True)
    state = serializers.PrimaryKeyRelatedField(read_only=True)
    city = serializers.PrimaryKeyRelatedField(read_only=True)
    school = serializers.PrimaryKeyRelatedField(read_only=True)
    commitment = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    '''This class is used for serialize offers'''

    schools = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    player = serializers.PrimaryKeyRelatedField(read_only=True)


