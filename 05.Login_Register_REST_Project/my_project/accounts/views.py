from django.shortcuts import render
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserCreate(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
