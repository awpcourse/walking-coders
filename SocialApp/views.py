from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from SocialApp.forms import UserForm, PostForm
from SocialApp.models import Post


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


def register(request):
    return render(request, 'register.html')


class HomeView(FormView, ListView):
    form_class = PostForm
    model = Post
    template_name = 'index.html'
    ordering = ["-date_added"]

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = Post(text=text, author=request.user)
            user_post.save()
        return redirect('index')
