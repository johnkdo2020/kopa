from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tours.models import ReviewComment, Place, Tag


class ReviewCommentSerializer(ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = ('id', 'review', 'user', 'title', 'content', 'password')


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class PlaceSerializer(ModelSerializer):
    tags = TagSerializer(many=True, source='tags.all')

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'content',
            'address',
            'average_score',
            'phone_number',
            'open_time',
            'url',
            'trans',
            'release_date',
            'tags'
        )


class PlaceDetailSerializer(ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'content',
            'address',
            'average_score',
            'phone_number',
            'open_time',
            'url',
            'trans',
            'release_date',
            'tags'
        )

    def get_tags(self, place):
        return place.tags.values_list('name', flat='True')
