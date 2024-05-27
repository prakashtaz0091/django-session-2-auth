from django.contrib.auth.models import User
from .models import Role
from django.contrib import messages
from django.shortcuts import redirect

def has_to_be_teacher(func):
    def wrapper_func(request, *args, **kwargs):
        teacher_role = Role.objects.get(name='teacher')

        if teacher_role in request.user.roles.all():
            return func(request, *args, **kwargs)
        else:
            messages.warning(request, 'You are not authorized to access this page')
            return redirect('accounts:home')
    return wrapper_func