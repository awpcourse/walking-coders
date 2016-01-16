from django.forms import Form, CharField, PasswordInput, DateField, ImageField
from django.contrib.admin.widgets import AdminDateWidget
from SocialApp.models import UserProfile


class UserForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserRegisterForm(UserForm):
    firstName = CharField(max_length=30)
    lastName = CharField(max_length=30)
    birthDate = DateField(widget=AdminDateWidget)
    avatar = ImageField()


class CompanyRegisterForm(UserForm):
    name = CharField(max_length=30)
    cover = ImageField()


class EditProfileForm(Form):
    fullname = CharField(required=True)
    birthdate = DateField()
    avatar = ImageField()
