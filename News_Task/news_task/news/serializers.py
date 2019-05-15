from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    model = News
    fields = '__all__'
