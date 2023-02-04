from django.db import models

# Creating user profile model.
class Courses(models.Model):
    courses = models.CharField(max_length= 100, blank=True)

    def __unicode__(self):
        return self.courses

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key = True)
    imgUrl = models.TextField()
    user_name = models.CharField(max_length=100)
    user_description = models.TextField()
    university_college = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, blank=True, null=True, on_delete=models.CASCADE)
    