from django.core.validators import RegexValidator
from django.db import models


class Message(models.Model):
    """
    Ordinary 'Contact Us' form.
    """

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    RECEIVED = 'rcv'
    PROCESSING = 'prc'
    REPLIED = 'rpl'
    STATUSES = (
        (RECEIVED, 'Получено'),
        (PROCESSING, 'В обработке'),
        (REPLIED, 'Ответ отправлен'),
    )

    first_name = models.CharField(
        'Имя', max_length=50, blank=False, null=False)
    last_name = models.CharField(
        'Фамилия', max_length=50, blank=False, null=False)
    email = models.EmailField('E-mail', blank=False, null=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Номер должен быть введён в формате Е.164.')
    phone_number = models.CharField(
        'Номер телефона',
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True)
    title = models.CharField(
        'Тема', max_length=100, blank=False, null=False)
    text = models.TextField(
        'Текст сообщения', blank=False, null=False)
    received_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=3, choices=STATUSES, default=RECEIVED)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.title} ({self.full_name})'
