from django.shortcuts import render, redirect
from blogs.models import Category,Blogs
from .forms import Registration_Form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_feachered=True, status='published')
    posts = Blogs.objects.filter(is_feachered=False, status='published')
    print(posts)

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts
    }
    return render(request,'home.html',context)

def register(request):
    if request.method == 'POST':
        form = Registration_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = Registration_Form()

    context={
        'form':form
    }
    return render (request,'register.html',context)

def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect ('home')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')
