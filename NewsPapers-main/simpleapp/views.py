from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class NewsList(ListView):
    model = Post

    ordering = 'name'

    template_name = 'post.html'

    context_object_name = 'post'
# Create your views here.
