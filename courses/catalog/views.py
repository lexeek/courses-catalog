from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CourseCreateForm

from django import forms
# from json_views.views import JSONListView, JSONDetailView
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json

from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from .models import Course


# Create your views here.

def course_create(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            messages.add_message(request, messages.INFO, 'Курс успешно добавлен')
            return render(request, 'form-add-course.html')

    else:
        form = CourseCreateForm()
    return render(request, 'form-add-course.html', {'form': form})


class CourseListView(ListView):
    queryset = Course.objects.all()
    template_name = 'index.html'

    # Filters function
    def get_queryset(self):
        query = self.request.GET.get('q')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        queryset = Course.objects.all()

        if query:
            queryset = queryset.filter(title__icontains=query)
        elif start_date:
            queryset = queryset.filter(start_date__gte=start_date)
        elif start_date:
            queryset = queryset.filter(end_date__lte=end_date)

        return queryset


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    template_name = 'course-detail.html'


class CourseDetailEdit(DetailView):
    queryset = Course.objects.all()
    template_name = 'course-detail.html'


# add new course to the database
def add_course(request):
    if request.method == "POST" and request.POST.get('title'):
        Course.objects.create(
            title=request.POST.get('title'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            number_of_lectures=request.POST.get('number_of_lectures'))

        messages.add_message(request, messages.INFO, 'Курс успешно добавлен')
    return render(request, 'form-add-course.html')


# delete a course
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course-delete-confirm.html'
    success_url = '/'

    def get(self, *a, **kw):
        return self.delete(*a, **kw)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'form-edit-course.html'
    fields = '__all__'


# class CourseForm(forms.ModelForm):
#
#     def add_course(self):
#         if self.method == "POST" and request.POST.get('title'):
#             Course.objects.create(
#                 title=self.POST.get('title'),
#                 start_date=self.POST.get('start_date'),
#                 end_date=self.POST.get('end_date'),
#                 number_of_lectures=self.POST.get('number_of_lectures'))
#
#         return render(self, "form-add-course.html")
#
#     def clean(self):
#         cleaned_data = super().clean()
#         start_date = cleaned_data.get("start_date")
#         end_date = cleaned_data.get("end_date")
#         if end_date < start_date:
#             raise forms.ValidationError("End date should be greater than start date.")


# def index(request):
#     queryset = Course.objects.all()
#     return JsonResponse(list(queryset), safe=False)
