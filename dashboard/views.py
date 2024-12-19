from django.shortcuts import render,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from . forms import FormsCategory,PostBlogForms
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from.forms import UsersAddForm, UserFormEdit

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()

    context = {
        'category_counts': category_counts,
        'blogs_count': blogs_count
    }

    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render (request, 'dashboard/categories.html')

def categories_add(request):
    if request.method == 'POST':
        form = FormsCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = FormsCategory()
    context = {
        'form': form
    }
    return render (request, 'dashboard/categories_add.html', context)


def categories_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = FormsCategory(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = FormsCategory(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render (request, 'dashboard/categories_edit.html', context)


def categories_remove(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blogs.objects.all()
    print(posts)
    context = {
        'posts': posts
    }
    return render (request, 'dashboard/posts.html', context)


def posts_add(request):
    if request.method == 'POST':
        form = PostBlogForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            print("sucess")
            return redirect('posts')
    else:
        print("Error")

    form = PostBlogForms()
    context = {
        'form': form
    }
    return render( request, "dashboard/posts_add.html",context)

def posts_edit(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    if request.method=="POST":
        form = PostBlogForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
    form = PostBlogForms(instance=post)
    context={
        'form':form,
        'post':post
    }
    return render(request, 'dashboard/posts_edit.html',context)



def posts_remove(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    all_users = User.objects.all()
    context = {
        'users': all_users
    }
    return render (request, 'dashboard/users.html',context)

def users_add(request):
    if request.method == 'POST':
        form = UsersAddForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to create a user
            return redirect('users')  # Redirect to a success page or another view
    else:
        form = UsersAddForm()
    
    context = {
        'form': form
    }
    return render(request, 'dashboard/users_add.html', context)

def users_edit(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserFormEdit(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = UserFormEdit(instance=user)
    context = {
        'form':form,
        'user': user
    }
    return render (request, 'dashboard/users_edit.html',context)

def users_remove(request,pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')


