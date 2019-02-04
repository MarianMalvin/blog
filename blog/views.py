from django.shortcuts import render

from blog.models import Post, Tag


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context=({'posts': posts}))


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context=({'post': post}))


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context=({'tags': tags}))


def tag_list(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/tag_list.html', context=({'posts': posts, 'tag': tag}))
