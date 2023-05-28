from rest_framework import serializers

from markers.models import AcceptedMarker, Image, MarkerProposal


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ['id', 'marker']


class AcceptedMarkerSerializer(serializers.ModelSerializer):
    marker_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = AcceptedMarker
        fields = '__all__'


class AcceptedMarkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedMarker
        exclude = ['description']


class MarkerProposalSerializer(serializers.ModelSerializer):
    marker_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = MarkerProposal
        fields = '__all__'

