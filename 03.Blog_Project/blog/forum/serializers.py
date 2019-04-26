from rest_framework import serializers
from .models import Question, Answer, Profile


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = 'id author content like dislike'.split()
        # read_only_fields = ('question', )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = 'id author question answers'.split()

    def create(self, validated_data):
        answer_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        Answer.objects.create(question=question, **answer_data)

        return question


class ProfileSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'email', 'questions']
