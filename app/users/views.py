from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from courses.views import SuperUserPassesTestMixin

from .models import Teacher
from .forms import TeacherCreationForm


class TeacherListView(ListView):
    model = Teacher


class AddTeacherView(SuperUserPassesTestMixin, CreateView):
    model = Teacher
    form_class = TeacherCreationForm
    extra_context = {'page_title': 'добавление нового преподавателя'}
    success_url = reverse_lazy('users:teachers_list')


class EditTeacherView(SuperUserPassesTestMixin, UpdateView):
    model = Teacher
    fields = ('first_name', 'last_name', 'bio',)
    extra_context = {
        'page_title': 'редактирование личных данных преподавателя'}
    success_url = reverse_lazy('users:teachers_list')
