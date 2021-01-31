from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Administrator, Teacher, Student


class AdministratorAdmin(UserAdmin):
    model = Administrator
    list_display = ('first_name', 'last_name', 'email',
                    'phone_number', 'is_active', 'is_staff')
    list_display_links = ('email',)
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'last_name')
    ordering = ('last_name', 'email')

    fieldsets = (
        ('Основная информация',
         {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Статус',
         {'fields': ('is_active', 'is_staff')})
    )
    add_fieldsets = (
        ('Основная информация',
         {'fields':
             ('email', 'first_name', 'last_name', 'password1', 'password2')}),
        ('Статус',
         {'fields': ('is_active', 'is_staff')})
    )


class TeacherAdmin(AdministratorAdmin):
    model = Teacher

    fieldsets = (
        ('Основная информация',
         {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Статус',
         {'fields': ('is_active',)}),
        ('Дополнительная информация',
         {'fields': ('bio',)})
    )
    add_fieldsets = (
        ('Основная информация',
         {'fields':
             ('email', 'first_name', 'last_name', 'password1', 'password2')}),
        ('Статус',
         {'fields': ('is_active',)}),
        ('Дополнительная информация',
         {'fields': ('bio',)})
    )


class StudentAdmin(AdministratorAdmin):
    model = Student

    fieldsets = (
        ('Основная информация',
         {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Статус',
         {'fields': ('is_active',)}),
        ('Дополнительная информация',
         {'fields': ('birth_date',)})
    )
    add_fieldsets = (
        ('Основная информация',
         {'fields':
             ('email', 'first_name', 'last_name', 'password1', 'password2')}),
        ('Статус',
         {'fields': ('is_active',)}),
        ('Дополнительная информация',
         {'fields': ('birth_date',)})
    )


admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
