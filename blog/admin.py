from django.contrib import admin

from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
