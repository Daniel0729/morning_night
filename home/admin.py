from django.contrib import admin
from home.models import Wakeup
# Register your models here.


class WakupModelAdmin(admin.ModelAdmin):
    list_display = ["wakeupmood","wakeuptime","wakeuptime_plan"]
    class Meta:
        model = Wakeup

admin.site.register(Wakeup,WakupModelAdmin)