from django.shortcuts import render
from rest_framework import viewsets
from user_profile.models import Courses, UserProfile
from user_profile.serializers import UserProfileSerializer, CoursesSerializer
# Use these two when you'll create url of one class inside another class
# from rest_framework.decorators import action
# from rest_framework.response import Response


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all(),
    serializer_class = UserProfileSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all(),
    serializer_class = CoursesSerializer