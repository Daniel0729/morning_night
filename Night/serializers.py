from Night.models import Light_State,Curtain_State
from rest_framework import serializers


class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Light_State
        fields = ('url','light')


class CurtainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curtain_State
        fields = ('url','curtain')