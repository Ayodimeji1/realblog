from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from post.models import Post

# Create your views here.


def index(request):
    featured = Post.objects.all()[:1]

    posts = Post.objects.filter(status='Published')[1:]

    paginator = Paginator(posts, 6)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'featured': featured,
        page: 'pages'
    }

    return render(request, 'core/index.html', context)


def archives(request):
    posts = Post.objects.filter(status='Published')[0:]

    paginator = Paginator(posts, 10)  # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        page: 'pages'
    }

    return render(request, 'core/archives.html', context)


def about(request):
    return render(request, 'core/about.html', {'about': about})


