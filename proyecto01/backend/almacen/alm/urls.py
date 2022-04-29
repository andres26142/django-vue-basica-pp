from rest_framework.routers import DefaultRouter
from django.urls import path, include

from alm.views import ClienteViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet)

urlpatterns = [
    path ('api/', include(router.urls)),
]