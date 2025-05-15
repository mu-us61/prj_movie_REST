from rest_framework import serializers
from app_watchlist.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ["watchlist"]


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

    review = ReviewSerializer(many=True, read_only=True)


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"

    watchlist = WatchListSerializer(many=True, read_only=True)
