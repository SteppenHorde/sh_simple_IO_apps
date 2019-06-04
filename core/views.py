from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import EmailForm



class Main(TemplateView):
    template_name = 'core/main.html'
    """
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        #return render(request, self.template_name, context=context)
        return context
    """


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # после регистрации переход на вход
    template_name = 'registration/signup.html'


class Profile(View):
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        context = {

        }

        return render(request, self.template_name, context=context)


class ChangeEmail(FormView):
    form_class = EmailForm
    template_name = 'user/change_email.html'

    def get(self, request, *args, **kwargs):
        self.user = User.objects.get(pk=request.user.pk)
        self.initial = {'email': self.user.email}
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.user = User.objects.get(pk=request.user.pk)
            self.user.email = self.request.POST['email']
            self.user.save()

        return render(request, self.template_name, {'form': form})
