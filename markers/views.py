from rest_framework import viewsets

from markers.models import AcceptedMarker
from markers.serializers import MarkerSerializer, MarkerListSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcceptedMarker.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return MarkerListSerializer
        else:
            return MarkerSerializer
