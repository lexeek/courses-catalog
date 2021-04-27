from django.urls import path

from .views import CourseListView, CourseDetailView, add_course

urlpatterns = [
    path('', CourseListView.as_view(), name='index'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add-course/', add_course, name='add_course'),
]

