from rest_framework import serializers

from markers.models import AcceptedMarker, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class MarkerSerializer(serializers.ModelSerializer):
    marker_images = ImageSerializer(many=True)

    class Meta:
        model = AcceptedMarker
        fields = '__all__'
