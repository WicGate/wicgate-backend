from rest_framework import serializers

from wicgate.replays.models import Replay


class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        exclude = []
