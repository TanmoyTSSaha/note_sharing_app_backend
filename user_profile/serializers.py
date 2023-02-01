from rest_framework import serializers
from user_profile.models import Courses, UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = UserProfile
        fields = '__all__'

class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'