from django.db import models

# Create your models here.
class CourseModel(models.Model):
    course_name=models.CharField(max_length=30)
    description=models.TextField()
    duration=models.CharField(max_length=10)
    fee=models.IntegerField()
    level=models.CharField(max_length=10)
    image=models.ImageField(upload_to="images",blank=True,null=True)
