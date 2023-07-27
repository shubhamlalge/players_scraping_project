from django.contrib import admin
from .models import Player, City, Class, Committment, School, State, Position, Offer

# Register your models here.
models = [Player, City, Class, Committment, State, School, Position, Offer]

admin.site.register(models)
