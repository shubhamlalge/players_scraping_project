from rest_framework import serializers
from .models import Player, City, Class, Committment, School, State, Position


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

    school = SchoolSerializer()

    class Meta:
        model = Committment
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    '''This class is used for serialize players'''

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
    '''This class is used for serialize offers'''

    schools = SchoolSerializer()
    player = PlayerSerializer()
