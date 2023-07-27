from django.db import models


class City(models.Model):
    '''This class used for create City table in db'''

    name = models.CharField(max_length=40, null=True, blank=True, unique=True, help_text="enter city name")


class Position(models.Model):
    '''This class used for create Position table in db'''
    name = models.CharField(max_length=40, null=True, blank=True, unique=True, help_text=" enter position field")


class State(models.Model):
    '''This class used for create State table in db'''
    name = models.CharField(max_length=40, null=True, blank=True, unique=True, help_text='enter state name')


class Class(models.Model):
    '''This class used for create Class table in db'''
    name = models.IntegerField(null=True, blank=True, unique=True, help_text='enter class name ')


class School(models.Model):
    '''This class used for create Schools table in db'''
    name = models.CharField(max_length=250, null=True, blank=True,
                            help_text='enter offer name  ')
    url = models.URLField(max_length=300, null=True, blank=True, help_text='enter offer logo url ')


class Committment(models.Model):
    '''This class used for create Commitment table in db'''
    recruiters = models.CharField(max_length=250, null=True, blank=True, help_text='enter recruiters names ')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, help_text='foreign key with school')


class Player(models.Model):
    '''This class used for create Player table in db'''
    image_url = models.URLField(max_length=300, null=True, blank=True,
                                help_text='enter player image url ')
    full_name = models.CharField(max_length=150, null=False, blank=False,
                                 help_text='enter player full name ')
    height = models.CharField(max_length=30, null=True, blank=True, help_text='enter player height ')
    weight = models.IntegerField(null=True, blank=True, help_text='enter player weight ')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, help_text='foreign key with player city ')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True,
                                 help_text='foreign key with player position ')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, help_text='foreign key with player state ')
    clas = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, help_text='foreign key with player class ')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, help_text='foreign key with school')
    commitment = models.ForeignKey(Committment, on_delete=models.SET_NULL, null=True,
                                   help_text='foreign key with commitment')


class Offer(models.Model):
    schools = models.ManyToManyField(School, help_text='many schools with many offer')
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, help_text='foreign key with player')
