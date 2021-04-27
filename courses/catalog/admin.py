from django.contrib import admin
from .models import Course

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'number_of_lectures')
    list_filter = ('title', 'start_date', 'end_date')
