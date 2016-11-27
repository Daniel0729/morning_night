from django.shortcuts import render,get_object_or_404,redirect
from home.models import Wakeup
from home.forms import WakeupForm
from django.contrib import messages


# Create your views here.
def home(request):
    instance = get_object_or_404(Wakeup)
    form = WakeupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #create some message
        messages.success(request,"Successfully add mood")
    else:
        messages.error(request,"something wrong")

    context = {
        "wakeuptime":instance.wakeuptime,
        "wakeuptime_plane": instance.wakeuptime_plan,
        "form":form,

    }

    return render(request,template_name='home/home.html',context=context)

