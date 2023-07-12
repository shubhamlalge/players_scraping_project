from django.contrib import admin
from .models import Player, City,Class,Commitment,School,State,Position,Offer,HighSchool
# Register your models here.
models = [Player,City,Class,Commitment,State,School,Position,Offer,HighSchool]

admin.site.register(models)