from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from SocialApp.forms import UserForm, EditProfileForm
from django.views.generic.edit import UpdateView
import pdb
from SocialApp.models import UserProfile


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
        pdb.set_trace()
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password, **kwargs)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)
        else:
            login(request, user)
            return redirect('index')


class EditProfileView(FormView):
    form_class = EditProfileForm
    template_name = 'editProfile.html'

    def get_context_data(self, **kwargs):
        context = super(EditProfileView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = EditProfileForm(request.POST)
        if form.is_valid():
            userprofile = UserProfile.objects.filter(id_user=request.user).update(name=form.fullname,
                                                                                  birthday=form.birthdate,
                                                                                  avatar=form.avatar)
            userprofile.save()
        else:
            form = EditProfileForm()
        return render(request, 'editProfile.html', form)


def register(request):
    return render(request, 'register.html')

