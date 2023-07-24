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


class OfferSerializer(serializers.ModelSerializer):
    '''This class is used for serialize offers'''
    # create school serializer object
    schools = SchoolSerializer(many=True)


class PlayerSerializer(serializers.ModelSerializer):
    '''This class is used for serialize players'''

    # create position serializer object
    position = PositionSerializer()
    # create class serializer object
    clas = ClassSerializer()
    # create state serializer object
    state = StateSerializer()
    # create city serializer object
    city = CitySerializer()
    # create school serializer object
    school = SchoolSerializer()
    # create commitment serializer object
    commitment = CommitmentSerializer()
    # create offer serializer object
    offer = OfferSerializer()

    class Meta:
        model = Player
        fields = '__all__'
