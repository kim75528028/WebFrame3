from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post,Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class PostList(ListView):
    model = Post
    #template_name = 'blog/post_list.html'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data() # post_list
        context['categories'] = Category.object.all()
        context['no_category_post_count'] = Post.object,filter(category=None).count()
        return context # post_list.html


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

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()  # post_list
        context['categories'] = Category.object.all()
        context['no_category_post_count'] = Post.object, filter(category=None).count()
        return context  # post_detail.html (post, categories,

#def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)
#    return render(
#        request,
#        'blog/post_detail.html',
#        {
#            'post': post,
#        }
#    )

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.object.filter(category=None)
    else:
        category = Category.object.get(slug=slug)
        post_list = Post.object.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.object.all(),
            'no_category_psot_count' : Post.object.filter(category=None).count(),
            'category' : category,
        }
    )

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags']
    # template_name = post_form.html

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self,form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')