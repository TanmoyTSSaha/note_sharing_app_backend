from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user_profile.views import UserProfileViewSet, CoursesViewSet

router = routers.DefaultRouter()
router.register(r'user_profile', UserProfileViewSet)
router.register(r'courses', CoursesViewSet)

urlpatterns = [
    path('', include(router.urls))

]
