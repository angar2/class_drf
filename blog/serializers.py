from unicodedata import category
from rest_framework import serializers
from blog.models import Article as ArticleModel
from blog.models import Category as CategoryModel
from blog.models import Comment as CommentModel


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentModel
        fields = ["author", "content"]


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
            model = CategoryModel
            fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, source="comment_set", read_only=True)
    category = serializers.SerializerMethodField()

    def get_category(self,obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        fields = ["author", "title", "body", "category", "comments"]