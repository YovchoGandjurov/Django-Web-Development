from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Question, Answer
from .serializers import QuestionSerializer


class QuestionList(APIView):
    """
    List all users, or create a new one.
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
    Retrieve, update or delete a user instance.
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
