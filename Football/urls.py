"""
Football app URLs.
"""
from django.urls import include, path
from rest_framework import routers
from Football import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'teams', views.FootballTeamViewSet)
router.register(r'stadiums', views.StadiumViewSet)
router.register(r'leagues', views.LeagueViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
