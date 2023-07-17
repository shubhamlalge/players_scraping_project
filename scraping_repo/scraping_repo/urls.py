from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from players.views import PlayerViewSet

router = DefaultRouter()
router.register('players', PlayerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('player/', include(router.urls)),

]
