from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('',
         views.CourseListView.as_view(), name='index'),
    path('courses/addcourse/',
         views.CourseAddView.as_view(), name='add_course'),
    path('courses/editcourse/<int:pk>',
         views.CourseEditView.as_view(), name='edit_course'),
    path('courses/deletecourse/<int:pk>',
         views.CourseDeleteView.as_view(), name='delete_course')
]
