from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Course
from .forms import CourseForm


class SuperUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class CoursesListView(ListView):
    model = Course


class AddCourseView(SuperUserPassesTestMixin, CreateView):
    model = Course
    form_class = CourseForm
    extra_context = {'page_title': 'добавление нового курса'}
    success_url = reverse_lazy('courses:index')


class EditCourseView(SuperUserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    extra_context = {'page_title': 'редактирование курса'}
    success_url = reverse_lazy('courses:index')
