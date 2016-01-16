from django.forms import Form, CharField, PasswordInput, DateField, ImageField
from django.contrib.admin.widgets import AdminDateWidget
from SocialApp.models import Role


class UserForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserRegisterForm(UserForm):
    ROLE_CHOICES = ('Company', 'Client')
    fullname = CharField(max_length=50)
    select_role = CharField(max_length=30)

