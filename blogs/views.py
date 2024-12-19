from django.shortcuts import render, HttpResponse, redirect
from . models import Blogs,Category, Comment
from django.shortcuts import  get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect


def posts_by_category(request,category_id):

    # Fetching the posts hat belongs to the category with category_id
    posts = Blogs.objects.filter(status='published', Category= category_id)

    try:
        category = Category.objects.get(pk=category_id) #use try and except when we want to do some custom actions if the category doesnot exist..
    except:
        return redirect('home')
    
    #category = get_object_or_404(category, pk=category_id) #use get_object_or_404 when you want to  show 404 error page if the categpry doesnot exist

    context = {
        'posts':posts,
        'category':category
    }
    return render(request, 'posts_by_category.html', context)

# blogs
def blogs(request, slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment= request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog=single_post)
    comments_count = comments.count()  # Count the total number of comments
    context = {
        'single_post': single_post,
        'comments': comments,
        'comments_count': comments_count,  # Pass count to the template
    }
    return render(request, 'blogs.html', context)


#search
def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    content = {  # Define content (it was previously context, both names are fine)
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', content)

