from django.contrib.auth.models import Group, User
from rest_framework import serializers

from Football.models import FootballTeam, League, Stadium


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StadiumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class FootballTeamSerializer(serializers.HyperlinkedModelSerializer):
    # stadium = StadiumSerializer()
    # league = LeagueSerializer()

    class Meta:
        model = FootballTeam
        fields = '__all__'
