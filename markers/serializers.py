from rest_framework import serializers

from markers.models import AcceptedMarker


class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedMarker
        fields = '__all__'
