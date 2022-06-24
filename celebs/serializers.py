from rest_framework import serializers
from .models import Celebs

class CelebsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Celebs
        # fields = ("title", "content", "cat")
        fields = ("__all__")