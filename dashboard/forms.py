from django import forms
from blogs.models import Category, Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormsCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')


class PostBlogForms(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','Category','blog_image', 'short_description','blog_body','status','is_feachered')

class UsersAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','is_active', 'is_staff', 'groups', 'user_permissions')

class UserFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email','is_active', 'is_staff', 'groups', 'user_permissions')