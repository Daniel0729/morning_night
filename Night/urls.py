from django.conf.urls import url,include
from . import views
from rest_framework import routers
from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'light',views.LightViewSet)
router.register(r'curtain',views.CurtainViewSet)

urlpatterns = [
    url(r'^Night/',views.detail,name="detail"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

]