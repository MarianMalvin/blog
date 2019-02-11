from django.shortcuts import render
from django.views import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context=({'posts': posts}))


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context=({'tags': tags}))


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'


class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
