from django import forms
from courses.models import Course


class AddCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_name'].widget.attrs.update({'class': 'form-group'})

    class Meta:
        model = Course
        fields = ('course_name',)

