from django.shortcuts import render
from rest_framework import viewsets

from markers.models import AcceptedMarker
from markers.serializers import AcceptedMarkerSerializer, AcceptedMarkerListSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcceptedMarker.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AcceptedMarkerListSerializer
        else:
            return AcceptedMarkerSerializer


def index(request):
    return render(request, 'markers/index.html')


def navod(request):
    return render(request, 'markers/navod.html')

def seznam(request):
    return render(request, 'markers/seznam.html')
