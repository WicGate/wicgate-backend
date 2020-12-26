from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from wicgate.replays.viewsets import ReplayViewSet
from wicgate.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("replays", ReplayViewSet)


app_name = "api"
urlpatterns = router.urls
