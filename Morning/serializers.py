from Morning.models import MLight_State,Music_State
from rest_framework import serializers


class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MLight_State
        fields = ('url','light')


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music_State
        fields = ('url','music')


