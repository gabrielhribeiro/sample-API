from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
# Create your views here.
