from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from blog.forms import TagForm
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

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form':form})
    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})
