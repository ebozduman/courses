from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Description(models.Model):
#     text = models.TextField()
#     course = models.OneToOneField(Course, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Comment(models.Model):
#     text = models.TextField()
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
