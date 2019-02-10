from django.shortcuts import render, get_object_or_404
from django.views import View
from .utils import ObjectDetailMixin
from blog.models import Post, Tag


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