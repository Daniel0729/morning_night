from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import Curtain_State,Light_State
from .serializers import LightSerializer,CurtainSerializer
from django.template import RequestContext
import requests
import json
# Create your views here.


class LightViewSet(viewsets.ModelViewSet):
    queryset = Light_State.objects.all()
    serializer_class = LightSerializer


class CurtainViewSet(viewsets.ModelViewSet):
    queryset = Curtain_State.objects.all()
    serializer_class = CurtainSerializer


def detail(request):
    out = ''
    lightstate = 'off'
    Curtain_State = 'close'
    if 'on' in request.POST:
        values = {"light": "on"}
        r = requests.put('http://127.0.0.1:8000/Night/light/1/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['light']
    if 'off' in request.POST:
        values = {"light": "off"}
        r = requests.put('http://127.0.0.1:8000/Night/light/1/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['light']
    if 'open' in request.POST:
        values = {"curtain": "open"}
        r = requests.put('http://127.0.0.1:8000/Night/curtain/3/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['curtain']
    if 'close' in request.POST:
        values = {"curtain": "stop"}
        r = requests.put('http://127.0.0.1:8000/Night/curtain/3/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['curtain']
    r = requests.get('http://127.0.0.1:8000/Night/light/1/',
                     auth=('syin', 'GODhm0608'))
    result = r.text
    output = json.loads(result)
    lightstate = output['light']
    r = requests.get('http://127.0.0.1:8000/Night/curtain/3/',
                     auth=('syin', 'GODhm0608'))
    result = r.text
    output = json.loads(result)
    curtainstate = output['curtain']

    return render(request, 'Night/detail.html', {'lightstate': lightstate, 'curtainstate': curtainstate})