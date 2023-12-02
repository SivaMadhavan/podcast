from rest_framework import serializers
from .models import *


class PodcastListSerializer(serializers.ModelSerializer):
    uploader = serializers.SerializerMethodField()

    class Meta:
        model = Podcast
        fields = "__all__"

    def get_uploader(self, instance):
        uploader = {}
        if getattr(instance, 'uploader'):
            uploader = {"username": instance.uploader.username, "pk": instance.uploader.pk}
        return uploader


class EpisodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"