from django.db import models


class City(models.Model):
    '''This class used for create City table in db'''
    name = models.CharField(max_length=40, null=True, blank=True) # city name field with max length 40


class Position(models.Model):
    '''This class used for create Position table in db'''
    position = models.CharField(max_length=40, null=True, blank=True) # position field with max length 40


class State(models.Model):
    '''This class used for create State table in db'''
    state = models.CharField(max_length=40, null=True, blank=True) # state field with max length 40


class Class(models.Model):
    '''This class used for create Class table in db'''
    class_ = models.IntegerField(max_length=30, null=True, blank=True) # class field with max length 30


class SchoolName(models.Model):
    '''This class used for create SchoolName table in db'''
    name = models.CharField(max_length=150, null=True, blank=True) # school name field with max length 150


class Team(models.Model):
    '''This class used for create Team table in db'''
    name = models.CharField(max_length=100, null=True, blank=True) # team name field with max length 100
    logo_url = models.URLField(max_length=300, null=True, blank=True) # team logo url field with max length 300


class Commitment(models.Model):
    '''This class used for create Commitment table in db'''
    team = models.ForeignKey(Team, on_delete=models.SET_NULL) # team model
    recruiters_name = models.CharField(max_length=300, null=True, blank=True) # recruiters names field


class Offer(models.Model):
    '''This class used for create  Offers table in db'''
    team = models.ForeignKey(Team, on_delete=models.SET_NULL) # team model


class Player(models.Model):
    '''This class used for create Player table in db'''
    image_url = models.URLField(max_length=300, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    height = models.CharField(max_length=30, null=True, blank=True)
    weight = models.IntegerField(max_length=30, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL) # city model
    position = models.ForeignKey(Position, on_delete=models.SET_NULL) # position model
    state = models.ForeignKey(State, on_delete=models.SET_NULL)# state model
    class_ = models.ForeignKey(City, on_delete=models.SET_NULL) # class model
    school_name = models.ForeignKey(SchoolName, on_delete=models.SET_NULL) # schoolname model
    offer = models.ManyToManyField(Offer) # make many to many  relation to offers
    commitment = models.ForeignKey(Commitment, on_delete=models.SET_NULL) # commitment model

