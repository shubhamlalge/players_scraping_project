from django.contrib import admin
from .models import Player, City, Class, Commitment, School, State, Position, Offer

# Register your models here.
models = [Player, City, Class, Commitment, State, School, Position, Offer]

admin.site.register(models)
