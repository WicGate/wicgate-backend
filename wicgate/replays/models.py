from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class Replay(models.Model):
    # Upload Details
    name = models.CharField(max_length=128, null=False, blank=False)
    submitter = models.CharField(max_length=32, null=False, blank=False)
    upload_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    tags = ArrayField(models.CharField(max_length=32, null=True, blank=True))
    description = models.TextField(null=True, blank=True)
    event = models.CharField(max_length=64, null=True, blank=True)
    series_count = models.IntegerField(null=True, blank=True)
    downloads = models.IntegerField(null=False, blank=False, default=0)
    # Replay Details
    map = models.CharField(max_length=32, null=False, blank=False)  # TODO: upgrade to choices
    vs = models.CharField(max_length=4, null=False, blank=False)
    type = models.CharField(max_length=32, null=False, blank=False)
    ranked = models.BooleanField(null=False, blank=False)
    game_date = models.DateTimeField(null=True, blank=True)
    mod = models.CharField(max_length=32, null=True, blank=True)
    winner = models.CharField(max_length=4, null=False, blank=False)  # TODO: upgrade to choices
    loser = models.CharField(max_length=4, null=False, blank=False)  # TODO: upgrade to choices
    winner_domination = models.IntegerField()
    loser_domination = models.IntegerField()
    winner_players = ArrayField(models.CharField(max_length=32, null=True, blank=True), size=8)
    loser_players = ArrayField(models.CharField(max_length=32, null=True, blank=True), size=8)
    scores = JSONField(null=True, blank=True)
    replay_name = models.CharField(max_length=32, null=True, blank=True)
    file_name = models.CharField(max_length=64, null=True, blank=True)
    view_side = models.CharField(max_length=4, null=True, blank=True)  # TODO: upgrade to choices
    view_player = models.CharField(max_length=32, null=True, blank=True)
    replay_length = models.CharField(max_length=5, null=True, blank=True)
    file = models.FileField(null=False, blank=False)  # upload-to

    def __str__(self):
        return '{name} by {submitter} ({vs} {map})'.format(
            name=self.name, submitter=self.submitter, vs=self.vs, map=self.map)
