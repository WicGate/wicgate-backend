from django.contrib import admin

from .models import Replay


@admin.register(Replay)
class ReplayAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'submitter', 'map', 'vs', 'winner', 'loser', 'downloads')
    list_filter = ('vs', 'map', 'submitter', 'upload_date', 'event')
    search_fields = ['name', 'submitter', 'description', 'event', 'map', 'vs', 'type',
                     'relay_name', 'file_name', 'upload_date']
    readonly_fields = ('upload_date',)
    fieldsets = (
        ('Upload Details', {
            'fields': (
                ('name', 'submitter', 'downloads'),
                ('event', 'series_count'),
                'upload_date',
                'tags',
                'description',
                'file'
            )
        }),
        ('Replay Details', {
            'fields': (
                ('map', 'vs'),
                'ranked',
                'game_date',
                ('type', 'mod',),
                ('winner', 'winner_domination', 'winner_players'),
                ('loser', 'loser_domination', 'loser_players'),
                'scores',
                ('replay_name', 'file_name'),
                ('view_side', 'view_player', 'replay_length'),
           )
        }),
    )
