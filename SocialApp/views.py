from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from SocialApp.forms import UserForm, UserRegisterForm
from SocialApp.models import User, UserProfile, Role
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


class LoginView(FormView):
    form_class = UserForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)
        else:
            login(request, user)
            return redirect('index')


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['roles'] = Role.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        fullname = request.POST['fullname']
        select_role = request.POST.get('select_role')
        if form.is_valid():
            new_user = form.save()
            UserProfile.objects.create(name=fullname,
                                       role=Role.objects.get(pk=select_role),
                                       id_user=new_user)
            return redirect('login')
        else:
            return redirect('register')

