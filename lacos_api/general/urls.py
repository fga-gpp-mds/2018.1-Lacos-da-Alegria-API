from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('hospital_activities', views.HospitalActivityViewSet)
router.register('ngo_activities', views.NGOActivityViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
