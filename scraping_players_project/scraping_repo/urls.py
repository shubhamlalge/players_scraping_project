from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from players.views import PlayerViewSet,ClassViewSet, SchoolViewSet,StateViewSet,PositionViewSet,CommitmentViewSet,\
    OfferViewSet,CityViewSet

router = DefaultRouter()

router.register('players', PlayerViewSet, basename='players')
router.register('class', ClassViewSet, basename='class')
router.register('school', SchoolViewSet, basename='school')
router.register('state', StateViewSet, basename='state')
router.register('position', PositionViewSet, basename='position')
router.register('commitment', CommitmentViewSet, basename='commitment')
router.register('offer', OfferViewSet, basename='offer')
router.register('city', CityViewSet, basename='city')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('users.urls')),

]
