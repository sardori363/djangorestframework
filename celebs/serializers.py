from rest_framework import serializers
from .models import Celebs

class CelebsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Celebs.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get("title", instance.title)
        instance.content = validate_data.get("content", instance.content)
        instance.time_update = validate_data.get("time_update", instance.time_update)
        instance.is_published = validate_data.get("is_published", instance.is_published)
        instance.cat_id = validate_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance