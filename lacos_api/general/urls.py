from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from lacos_api.user_api.views import UserProfileViewSet
from lacos_api.user_api.views import LoginViewSet
from lacos_api.activity_api.views import HospitalActivityViewSet
from lacos_api.activity_api.views import NGOActivityViewSet


router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name='login')
router.register('hospital-activities', HospitalActivityViewSet)
router.register('ngo-activities', NGOActivityViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
