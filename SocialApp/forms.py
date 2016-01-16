from django.forms import Form, CharField, PasswordInput, DateField, ImageField
from django.contrib.admin.widgets import AdminDateWidget


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
