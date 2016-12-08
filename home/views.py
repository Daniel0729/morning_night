from django.shortcuts import render,get_object_or_404,redirect
from home.models import Wakeup
from home.forms import WakeupForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    instance =Wakeup.objects.last()
    context = {
        "wakeuptime":instance.wakeuptime,
        "wakeuptime_plan": instance.wakeuptime_plan,
        "wakeup_mood":instance.wakeupmood,
    }
    return render(request,template_name='home/home.html',context=context)
def submitmood(request):
    form = WakeupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context1 = {
        "form":form
    }
    return render(request, template_name='home/submit.html', context=context1)

def pullstatistics(request):
    queryset = Wakeup.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request,template_name='home/Stats.html',context=context)
