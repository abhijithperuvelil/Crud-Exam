from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app import serializers
from app.serializers import CourseSerializer
from app.models import CourseModel


# Create your views here.
class ListCreateCourse(APIView):
    def get(self,request):
        c=CourseModel.objects.all()
        serializer_instance=CourseSerializer(c,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer_instance=CourseSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class RetrieveDeleteUpdate(APIView):
    def get(self,request,i):
        c=get_object_or_404(CourseModel,id=i)
        serializers_instance=CourseSerializer(c)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)
    def put(self,request,i):
        c=get_object_or_404(CourseModel,id=i)
        serializers_instance=CourseSerializer(instance=c,data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_404_NOT_FOUND)
    def patch(self,request,i):
        c=get_object_or_404(CourseModel,id=i)
        serializers_instance=CourseSerializer(instance=c,data=request.data,partial=True)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,i):
        c=get_object_or_404(CourseModel,id=i)
        c.delete()
        return Response({"message":"deleted"})
