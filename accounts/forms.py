from django import forms
from accounts.models import Staff, Student
class AddStaffForm(forms.ModelForm):
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

