from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .import views

app_name = 'users'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(), name='logout'),
    path('teachers/',
         views.TeacherListView.as_view(), name='teachers_list'),
    path('teachers/add/',
         views.TeacherAddView.as_view(), name='add_teacher'),
    path('teachers/edit/<int:pk>',
         views.TeacherEditView.as_view(), name='edit_teacher'),
    path('teachers/delete/<int:pk>',
         views.TeacherDeleteView.as_view(), name='delete_teacher'),
]
