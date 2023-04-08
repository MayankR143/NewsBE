from rest_framework import serializers
from news_crud.models import NewsModel

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'user.username')
    user_updated = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = NewsModel
        fields = (
            'id',
            'name',
            'description',
            'author',
            'source',
            'image',
            'date',
            'date_created',
            'date_updated',
            'user_updated',
        )
    
    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if not request or not hasattr(request, "user"):
            raise ValueError("You are not authenticated")
        user = request.user
        validated_data["author"] = user
        validated_data["user_updated"] = user
        news = NewsModel(**validated_data)
        news.save()
        return news
    
    def update(self, instance, validated_data):
        user = None
        request = self.context.get("request")
        if not request or not hasattr(request, "user"):
            raise ValueError("You are not authenticated")
        user = request.user
        instance.user_updated = user
        for key, value in validated_data:
            if hasattr(instance, key):
                setattr(instance, key, value)
        instance.save()
        return instance