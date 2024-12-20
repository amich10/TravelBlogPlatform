from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Registration_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
