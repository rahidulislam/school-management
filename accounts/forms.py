
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser, Staff, Student


class CreateUserForm(UserCreationForm):
    address = forms.CharField()
    profile_image = forms.ImageField()
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', )











class StaffUpdateForm(forms.ModelForm):
    first_name = forms.CharField( max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=255, required=True)
    profile_image = forms.ImageField(required=True)

    class Meta:
        model = Staff
        fields = ("first_name", "last_name", "username", "email", "password", "address", "profile_image" )

class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField( max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=100, required=True)



    class Meta:
        model = Student
        fields = ("first_name", "last_name", "username", "email", "password","gender", "address","course","session_start","session_end", "profile_image" )


class StudentUpdateForm(forms.ModelForm):
    first_name = forms.CharField( max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=100, required=True)



    class Meta:
        model = Student
        fields = ("first_name", "last_name", "username", "email", "password","gender", "address","course","session_start","session_end", "profile_image" )

