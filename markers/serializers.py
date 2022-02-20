from rest_framework import serializers

from markers.models import AcceptedMarker, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ['id', 'marker']


class MarkerSerializer(serializers.ModelSerializer):
    marker_images = ImageSerializer(many=True)

    class Meta:
        model = AcceptedMarker
        fields = '__all__'

