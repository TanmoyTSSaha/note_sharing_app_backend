from django.contrib import admin
from user_profile.models import Courses, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Courses)
