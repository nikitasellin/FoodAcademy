from django.contrib.auth.forms import UserCreationForm


from .models import Teacher


class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('email', 'first_name', 'last_name', 'bio')
