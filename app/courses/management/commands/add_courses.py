from random import choice, randint

from django.core.management import BaseCommand
from factory import django, Faker

from courses.models import Course
from users.models import Teacher


class CourseFactory(django.DjangoModelFactory):
    class Meta:
        model = Course

    title = Faker('job')
    description = Faker('text', max_nb_chars=1000, ext_word_list=None)


def add_course(factory, teachers):
    course = factory.create()
    for teacher_id in range(randint(1, teachers.count())):
        teacher = choice(teachers)
        course.teachers.add(teacher)


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_teachers = Teacher.objects.all()
        if not all_teachers:
            print('Сначала добавьте пользователей')
            return
        if Course.objects.all():
            print('Курсы уже добавлены')
            return
        with Faker.override_default_locale('ru_RU'):
            course_factory = CourseFactory
            for c in range(5):
                add_course(course_factory, all_teachers)
        print('Курсы успешно добавлены')
