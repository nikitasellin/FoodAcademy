from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from courses.views import SuperUserPassesTestMixin

from .models import Teacher
from .forms import TeacherForm


class TeacherListView(ListView):
    model = Teacher


class TeacherAddView(SuperUserPassesTestMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    extra_context = {'page_title': 'добавление нового преподавателя'}
    success_url = reverse_lazy('users:teachers_list')


class TeacherEditView(SuperUserPassesTestMixin, UpdateView):
    model = Teacher
    fields = ('first_name', 'last_name', 'bio',)
    extra_context = {
        'page_title': 'редактирование личных данных преподавателя'}
    success_url = reverse_lazy('users:teachers_list')


class TeacherDeleteView(SuperUserPassesTestMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('users:teachers_list')
