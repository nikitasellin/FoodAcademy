from django.contrib.auth.forms import UserCreationForm


from .models import Teacher


class TeacherForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('email', 'first_name', 'last_name', 'avatar', 'bio')
