from django.contrib.admin.widgets import AdminDateWidget
from django.forms import Form, CharField, PasswordInput, DateField, ImageField, Textarea
from SocialApp.models import Role


class UserForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class CompanyRegisterForm(UserForm):
    name = CharField(max_length=30)
    cover = ImageField()


class PostForm(Form):
    text = CharField(widget=Textarea(
            attrs={'cols': 100, 'rows': 5, 'placeholder': "Say something"}),
            label='')


class MessageForm(Form):
    username = CharField(max_length=80)
    text = CharField(widget=Textarea(
            attrs={'cols': 100, 'rows': 5, 'placeholder': "What's on your mind?"}),
            label='')

