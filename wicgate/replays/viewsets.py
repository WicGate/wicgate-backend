from rest_framework import viewsets, permissions, filters

from wicgate.replays.models import Replay
from wicgate.replays.serializers import ReplaySerializer


class ReplayViewSet(viewsets.ModelViewSet):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'submitter', 'tags', 'event', 'map', 'vs', 'type', 'winner_players',
                     'loser_players', 'winner', 'loser', 'upload_date', 'replay_name', 'file_name',
                     'game_date', 'view_side', 'view_player', 'mod']
    offset_query_param = 'offset'
    limit_query_param = 'limit'
    max_limit = 1000

    def get_queryset(self):
        # /api/replays/?search=&sort=id&order=desc&offset=0&limit=50
        sort = self.request.query_params.get('sort', None)
        order = self.request.query_params.get('order', None)
        if order is None and sort is None:
            return Replay.objects.order_by('-pk')

        order_query = ''
        if order is not None and order == 'desc':
            order_query += '-'
        if sort is not None:
            order_query += 'pk' if sort == 'id' else sort

        return Replay.objects.all().order_by(order_query)
