from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)

from .models import Post, Comment

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    



class BlogCreateView(CreateView):
    model = Post
    template_name = "create.html"
    fields = ['title', 'author', 'body',]
    

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html' 
    fields  = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('blog:home')


# VIEWS FOR THE COMMENT

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields = ['content']

class CommentListView(ListView):
    model = Comment
    template_name = 'comment.html'

