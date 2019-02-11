from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(text):
    new_slug = slugify(text, allow_unicode=True)
    return f"{new_slug}-{str(int(time()))[:4]}"


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('tag_list_url', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('tag_edit_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    date_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('post_edit_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
