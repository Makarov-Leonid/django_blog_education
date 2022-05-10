from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from blog.utils import ObjectDetailMixin, ObjCreateMixin, ObjUpdateMixin, ObjDeleteMixin


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


class TagUpdate(ObjUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'


class PostUpdate(ObjUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'


class TagDelete(ObjDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'


class PostDelete(ObjDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'
