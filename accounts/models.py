from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.managers import UserManager
from courses.models import Course

from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.


class User(AbstractUser):
    ADMIN = 1
    TEACHER = 2
    STUDENT = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),

    )

    username = None
    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    mobile = models.CharField(max_length=20)
    address = models.TextField()
    profile_image = models.ImageField(upload_to="profile/", blank=True)

    def __str__(self):
        return self.user.email






