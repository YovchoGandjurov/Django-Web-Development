from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionsList(APIView):
    """
    List all question, or create a new one.
    """

    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """
    Retrieve, update or delete a question instance.
    """
    def get_object(self, pk):
        # obj = get_object_or_404(Question, pk=pk)
        # return obj
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404()

    def get(self, request, question_id):
        question = self.get_object(pk=question_id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, question_id):
        question = self.get_object(pk=question_id)
        serializer = QuestionSerializer(question, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        question = self.get_object(pk=question_id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswersList(APIView):
    """
    List all answers, or create a new one.
    """
    def get(self, request, question_id):
        answer = Answer.objects.filter(question_id=question_id)
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)

    def post(self, request, question_id):
        serializer = AnswerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetail(APIView):
    """
    Retrieve, update or delete a answer instance.
    """
    def get_object(self, answer_id, question_id):
        # Another way without get_object:
        # answer = get_object_or_404(Answer, pk=answer_id,
        #                            question_id=question_id)

        try:
            return Answer.objects.get(pk=answer_id, question_id=question_id)
        except Answer.DoesNotExist:
            raise Http404()

    def get(self, request, question_id, answer_id):
        url_path = request.get_full_path()

        answer = self.get_object(answer_id, question_id)
        serializer = AnswerSerializer(answer)

        if 'dislike' in url_path:
            answer.dislike += 1
            answer.save()
            return Response(serializer.data)

        elif 'like' in url_path:
            answer.like += 1
            answer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.data)

    def put(self, request, question_id, answer_id):
        answer = self.get_object(answer_id=answer_id, question_id=question_id)
        serializer = AnswerSerializer(answer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id, answer_id):
        answer = self.get_object(answer_id=answer_id, question_id=question_id)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
