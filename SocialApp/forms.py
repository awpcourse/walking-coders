from django.contrib.admin.widgets import AdminDateWidget
from django.forms import Form, CharField, PasswordInput, DateField, ImageField, Textarea


class UserForm(Form):
    userName = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserRegisterForm(UserForm):
    firstName = CharField(max_length=30)
    lastName = CharField(max_length=30)
    birthDate = DateField(widget=AdminDateWidget)
    avatar = ImageField()


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
