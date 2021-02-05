from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('',
         views.CoursesListView.as_view(), name='index'),
    path('courses/addcourse/',
         views.AddCourseView.as_view(), name='add_course'),
    path('courses/edit_course/<int:pk>',
         views.EditCourseView.as_view(), name='edit_course')
]
