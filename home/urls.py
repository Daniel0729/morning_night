from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home,name = 'home'),
    url(r'^submit/',views.submitmood,name = "submit"),
    url(r'^Stats/',views.pullstatistics,name = "submit")
]