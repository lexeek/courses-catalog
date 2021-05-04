from django import forms
from .models import Course


# testing forms
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'start_date', 'end_date', 'number_of_lectures')