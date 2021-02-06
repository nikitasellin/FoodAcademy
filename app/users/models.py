from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

from .managers import CommonUserManager


class CommonUser(AbstractUser):
    """
    Custom user model (authorization via e-mail).
    # TODO! Add avatar before creating views.
    """

    username = None
    first_name = models.CharField(
        'Имя', max_length=50, blank=False, null=False)
    last_name = models.CharField(
        'Фамилия', max_length=50, blank=False, null=False)
    email = models.EmailField(
        'E-mail', unique=True, blank=False, null=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Номер должен быть введён в формате Е.164.')
    phone_number = models.CharField(
        'Номер телефона',
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CommonUserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Administrator(CommonUser):
    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'


class Teacher(CommonUser):
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    bio = models.TextField('Биография', blank=True, null=True)


class Student(CommonUser):
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    birth_date = models.DateField('День рождения', blank=True, null=True)
