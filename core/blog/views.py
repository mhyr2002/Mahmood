from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from blog.models import Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# from hitcount.views import HitCountDetailView
# from hitcount.models import HitCount
 
# Create your views here.

"""fucntion to manage main page of blog :page/category/author"""
def blog_view (request,**kwargs):
    posts = Post.objects.filter(status = 1)
    if kwargs.get('cat_name')!= None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!= None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name')!= None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts,6)

    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context =  {'posts' :posts}
    return render(request,'blog/blog-home.html',context)



"""fucntion to manage single page of blog"""
def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment did not submit')

    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    categories = post.category.all()
    similar_post = posts.filter(category__in=categories).exclude(pk=post.pk)
    post.counted_view += 1
    post.save() 
    comments = Comment.objects.filter(post=post.id, approved=True)
    form = CommentForm()
    
    # Create a HitCount object for the post
    # hit_count, created = HitCount.objects.get_or_create(content_object=post)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'similar_post' :similar_post,
        
    }

    if not post.login_require:
        return render(request, 'blog/blog-single.html', context)
    else:
        if request.user.is_authenticated:
            return render(request, 'blog/blog-single.html', context)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))




"""funciton for search in content of blog"""
def blog_search (request): 
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        if s:= request.GET.get('search'):
            posts = posts.filter(Q(title__icontains=s) | Q(content__icontains=s))
    posts = Paginator(posts,6)

    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context =  {'posts' :posts}
    return render(request,'blog/search-result.html',context)