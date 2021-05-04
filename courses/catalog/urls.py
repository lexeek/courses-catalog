from django.urls import path

from .views import CourseListView, CourseDetailView, CourseDeleteView, add_course, course_create, CourseUpdateView

urlpatterns = [
    path('', CourseListView.as_view(), name='index'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add-course/', course_create, name='add_course_form'),
    path('<int:pk>/delete/', CourseDeleteView.as_view()),
    path('<int:pk>/edit/', CourseUpdateView.as_view()),
]
