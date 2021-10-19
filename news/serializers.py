from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from .models import Article, Journalist

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(max_length=255)
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=255)
#     body = serializers.CharField(max_length=255)
#     active = serializers.BooleanField(default=True)
#     location = serializers.CharField(max_length=255)
#     published = serializers.DateField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.published = validated_data.get('published', instance.published)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#
#     def validate(self, data):
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description must be different")
#         return data



class ArticleSerializer(serializers.ModelSerializer):

    time_published = serializers.SerializerMethodField()
    # author = JournalistSerializer()
    class Meta:
        model = Article
        exclude = ("id", )

    def get_time_published(self, object):
        published = object.published
        now = datetime.now()
        time_dalta = timesince(published, now)
        return time_dalta

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different")
        return data


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")
    # articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Journalist
        fields = "__all__"