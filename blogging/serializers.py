from django.contrib.auth.models import User
from blogging.models import Post, Category
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "author",
            "created_date",
            "modified_date",
            "published_date",
        ]


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
