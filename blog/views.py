from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views import View

from blog.forms import PostForm, TagForm
from blog.models import Post, Tag
from .utils import *


def post_list(request):
    paginator = Paginator(Post.objects.all(), 5)
    page = paginator.get_page(request.GET.get('page', 1))
    return render(request, 'blog/index.html', context=({'page': page, 'current_page': page.number}))


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context=({'tags': tags}))


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    template = 'blog/post_update.html'
    model_form = PostForm
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    template = 'blog/tag_update.html'
    model_form = TagForm
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True
