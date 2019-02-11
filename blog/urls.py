from django.urls import path

from .views import *

urlpatterns = [
    path('', post_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/slug/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/edit/<str:slug>/', PostUpdate.as_view(), name='post_edit_url'),
    path('post/delete/<str:slug>/', PostDelete.as_view(), name='post_delete_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/slug/<str:slug>/', TagDetail.as_view(), name='tag_list_url'),
    path('tag/edit/<str:slug>/', TagUpdate.as_view(), name='tag_edit_url'),
    path('tag/delete/<str:slug>/', TagDelete.as_view(), name='tag_delete_url'),
    path('tags/', tags_list, name='tags_list_url')
]
