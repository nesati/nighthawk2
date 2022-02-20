from rest_framework import viewsets

from markers.models import AcceptedMarker
from markers.serializers import MarkerSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcceptedMarker.objects.all()
    serializer_class = MarkerSerializer
