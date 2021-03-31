# from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from Football.models import FootballTeam, League, Stadium
from Football.serializers import (
    FootballTeamSerializer,
    GroupSerializer,
    LeagueSerializer,
    StadiumSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class FootballTeamViewSet(viewsets.ModelViewSet):
    queryset = FootballTeam.objects.all()
    serializer_class = FootballTeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [permissions.IsAuthenticated]
