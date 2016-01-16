import pdb

from django.http import HttpResponse

from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from SocialApp.forms import PostForm
from SocialApp.models import Post

from SocialApp.forms import UserForm, MessageForm, EditProfileForm
from SocialApp.models import Message, User, UserProfile, Role

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


class MessageView(FormView, ListView):
    model = Message
    form_class = MessageForm
    template_name = 'message_list.html'

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def get_queryset(self):
        message = Message.objects.all().filter(to_user=self.request.user)
        return message

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = Post(text=text, author=request.user)
            user_post.save()
            user_name = form.cleaned_data['username']
            to_user = User.objects.get(username=user_name)
            if to_user != request.user:
                if to_user is not None:
                    message = Message(from_user=request.user, to_user=to_user, content=text, received='Test')
                    message.save()
                    return redirect('message')
                else:
                    return HttpResponse('Nu avem user')
            else:
                return HttpResponse('Error')
