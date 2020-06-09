from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from courses.models import Course


class CustomUser(AbstractUser):
    USER_TYPE = (
        (1, 'HOD'),
        (2, 'Staff'),
        (3, 'Student'),
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE, default=1)


class AdminHOD(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pic/')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.get_full_name()


class Student(models.Model):
    GENDER_TYPE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_TYPE, max_length=10, default='male')
    profile_image = models.ImageField(upload_to='profile_pic/')
    address = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True, null=True)
    session_start = models.DateField(null=True)
    session_end = models.DateField(null=True)



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)

        if instance.user_type == 2:
            Staff.objects.create(admin=instance)

        if instance.user_type == 3:
            Student.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()

    if instance.user_type == 2:
        instance.staff.save()

    if instance.user_type == 3:
        instance.student.save()



