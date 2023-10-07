from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class RegistrationView(CreateView):

    model = USER_MODEL
    form_class = UserCreationForm
    template_name = "registration/form.html"
    success_url = reverse_lazy("login")
