'''
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post #post_list
    # template_name = 'blog/index.html'
    ordering = '-pk'
# def index(request):
#     posts = Post.objects.all().order_by('pk')
#
#     return render(
#         request, 'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single_post_pages.html'

# def single_post_pages(request,pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/single_post_pages.html',
#         {
#             'post': post,
#         }
#     )
'''
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    #template_name = 'blog/post_list.html'
    ordering = '-pk'

#def index(request):
#    posts = Post.objects.all().order_by('-pk')
#
#    return render(
#        request, 'blog/post_list.html',
#        {
#            'posts': posts,
#        }
#    )

class PostDetail(DetailView):
    model = Post

#def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)
#    return render(
#        request,
#        'blog/post_detail.html',
#        {
#            'post': post,
#        }
#    )
