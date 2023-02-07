from django.db import models

# Creating user profile model.
class Courses(models.Model):
    courses = models.CharField(max_length= 100, blank=True)

    def __str__ (self):
        return self.courses

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key = True)
    img = models.ImageField(upload_to='profile_picture', blank=True)
    user_name = models.CharField(max_length=100)
    user_description = models.TextField()
    university_college = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)