from django.core.management import BaseCommand
from factory import django, Faker, PostGenerationMethodCall

from users.models import CommonUser, Teacher


class CommonUserFactory(django.DjangoModelFactory):
    class Meta:
        model = CommonUser

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    password = PostGenerationMethodCall('set_password', 'password')
    phone_number = Faker('msisdn')


class TeacherFactory(CommonUserFactory):
    class Meta:
        model = Teacher

    bio = Faker('text', max_nb_chars=500, ext_word_list=None)


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Teacher.objects.all():
            print('Пользователи уже добавлены')
            return
        with Faker.override_default_locale('ru_RU'):
            for i in range(5):
                factory = TeacherFactory
                factory.create()
        print('Пользователи успешно добавлены')
