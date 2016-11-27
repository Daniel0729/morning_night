from django.shortcuts import render
#from .forms import LightState_Form,Music_State
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from Morning.models import Music_State,MLight_State
from Morning.serializers import LightSerializer,MusicSerializer
#from django.serializers import RequestContext
import requests
import json
# Create your views here.


class LightViewSet(viewsets.ModelViewSet):
    queryset = MLight_State.objects.all()
    serializer_class = LightSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music_State.objects.all()
    serializer_class = MusicSerializer


def detail(request):
    out = ''
    lightstate = 'off'
    musicstate = 'stop'
    if 'on' in request.POST:
        values = {"light": "on"}
        r = requests.put('http://127.0.0.1:8000/Moring/light/1/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['light']
    if 'off' in request.POST:
        values = {"light": "off"}
        r = requests.put('http://127.0.0.1:8000/Morning/light/1/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['light']
    if 'play' in request.POST:
        values = {"music": "play"}
        r = requests.put('http://127.0.0.1:8000/Morning/music/1/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['music']
    if 'stop' in request.POST:
        values = {"music": "stop"}
        r = requests.put('http://127.0.0.1:8000/Morning/music/1/',
                         data=values, auth=('syin', 'GODhm0608'))
        result = r.text
        output = json.loads(result)
        out = output['music']
    r = requests.get('http://127.0.0.1:8000/Morning/light/1/',
                     auth=('syin', 'GODhm0608'))
    result = r.text
    output = json.loads(result)
    lightstate = output['light']
    r = requests.get('http://127.0.0.1:8000/Morning/music/1/',
                     auth=('syin', 'GODhm0608'))
    result = r.text
    output = json.loads(result)
    musicstate = output['music']

    return render(request, 'Morning/detail.html', {'lightstate': lightstate, 'musicstate': musicstate})
# def detail(request):
#     return render(request,'Morning/detail.html')
#
# def get_light(request):
#     form = LightState_Form(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#
#     context = {
#         "form": form,
#
#     }
#     return render(request,template_name="Morning/detail.html", context=context)
#
# def get_music(request):
#     form = Music_State(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#
#     context = {
#         "form": form,
#
#     }
#     return render(request,template_name="Morning/detail.html", context=context)