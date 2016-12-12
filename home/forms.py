from django import forms
from home.models import Wakeup

# wakeup_mood = ('good','natural','bad')
class WakeupForm(forms.ModelForm):
     class Meta:
         model = Wakeup
         fields =["wakeupmood"]


