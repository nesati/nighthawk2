from rest_framework import serializers

from markers.models import AcceptedMarker, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ['id', 'marker']


class MarkerSerializer(serializers.ModelSerializer):
    marker_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = AcceptedMarker
        fields = '__all__'


class MarkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedMarker
        exclude = ['description']

