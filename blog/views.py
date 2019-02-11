from django.views import View

from blog.forms import PostForm
from blog.models import Post, Tag
from .utils import *


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context=({'posts': posts}))


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context=({'tags': tags}))


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    template = 'blog/tag_update.html'
    model_form = TagForm


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    template = 'blog/post_update.html'
    model_form = PostForm
