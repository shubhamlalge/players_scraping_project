from django.db import models


class City(models.Model):
    '''This class used for create City table in db'''

    name = models.CharField(max_length=40, null=True, blank=True, unique=True)  # city name field with max length 40


class Position(models.Model):
    '''This class used for create Position table in db'''
    position = models.CharField(max_length=40, null=True, blank=True, unique=True)  # position field with max length 40


class HighSchool(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)  # high school name field with max length 250


class State(models.Model):
    '''This class used for create State table in db'''
    state = models.CharField(max_length=40, null=True, blank=True, unique=True)  # state field with max length 40


class Class(models.Model):
    '''This class used for create Class table in db'''
    classes = models.IntegerField(null=True, blank=True, unique=True)  # class field with max length 30


class School(models.Model):
    '''This class used for create SchoolName table in db'''
    name = models.CharField(max_length=250, null=True, blank=True)  # team name field with max length 250
    url = models.URLField(max_length=300, null=True, blank=True)  # team logo url field with max length 300


class Offer(models.Model):
    '''This class used for create Team table in db'''
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)


class Commitment(models.Model):
    '''This class used for create Commitment table in db'''
    recruiters = models.CharField(max_length=250, null=True, blank=True)  # recruiters names field
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)


class Player(models.Model):
    '''This class used for create Player table in db'''
    image_url = models.URLField(max_length=300, null=True, blank=True)
    full_name = models.CharField(max_length=150, null=False, blank=False)
    height = models.CharField(max_length=30, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)  # city model
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)  # position model
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)  # state model
    clas = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)  # class model
    high_school = models.ForeignKey(HighSchool, on_delete=models.SET_NULL, null=True)  # school-name model
    offer = models.ManyToManyField(Offer)  # make many-to-many  relation to offers
    commitment = models.ForeignKey(Commitment, on_delete=models.SET_NULL, null=True)  # commitment model
