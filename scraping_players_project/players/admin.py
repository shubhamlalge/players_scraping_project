from django.contrib import admin
from .models import Player, City, Class, Committed, School, State, Position, Offer

# Register your models here.
models = [Player, City, Class, Committed, State, School, Position, Offer]

admin.site.register(models)
