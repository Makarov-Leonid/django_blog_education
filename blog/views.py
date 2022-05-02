from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from blog.utils import ObjectDetailMixin, ObjCreateMixin


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagCreate(ObjCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class PostCreate(ObjCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
