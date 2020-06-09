from django.db import models
from django.urls import reverse



class Course(models.Model):

    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

class Subject(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=255)
    staff = models.ForeignKey('accounts.Staff', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse("courses:subject_detail", kwargs={"pk": self.pk})