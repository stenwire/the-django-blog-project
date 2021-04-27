from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    CommentCreateView,
    CommentListView,
)

app_name = "blog"

urlpatterns = [
    path('post/comment/', CommentListView.as_view(), name = "comment_view"),
    path('post/create/<int:pk>/', CommentCreateView.as_view(), name="comment_create"),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name="post_edit"),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('', BlogListView.as_view(), name="home"),
    path('post/<int:pk>', BlogDetailView.as_view(), name="post_detail"),  
]
