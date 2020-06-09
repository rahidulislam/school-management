from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser, Staff, Student
# Register your models here.
class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser, UserModel)
admin.site.register(Staff)
admin.site.register(Student)