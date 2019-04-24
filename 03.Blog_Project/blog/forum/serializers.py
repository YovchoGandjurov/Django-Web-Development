from rest_framework import serializers
from .models import Question
from .models import Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = 'id author question'.split()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = 'id author content like dislike'.split()
