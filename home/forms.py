from django import forms
from home.models import Wakeup


class WakeupForm(forms.ModelForm):
    class Meta:
        model = Wakeup
        fields = [
            "wakeupmood",
        ]