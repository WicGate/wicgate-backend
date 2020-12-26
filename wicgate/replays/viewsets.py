from rest_framework import viewsets, permissions

from wicgate.replays.models import Replay
from wicgate.replays.serializers import ReplaySerializer


class ReplayViewSet(viewsets.ModelViewSet):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

