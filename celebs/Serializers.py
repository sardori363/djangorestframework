from rest_framework import serializers

from .models import Celebs


class CelebsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebs
        fields = ('title', 'cat_id')
