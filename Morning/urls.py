from django.conf.urls import url,include
from .views import MusicViewSet,LightViewSet
from rest_framework import routers
from django.contrib import admin
from . import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'music',MusicViewSet)
router.register(r'light',LightViewSet)

urlpatterns = [
    url(r'^Morning/',views.detail,name="detail"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

]