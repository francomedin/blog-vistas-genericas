from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ['autor', 'titulo', 'texto']
    success_url = reverse_lazy('post_list')


class PostListView(ListView):
    queryset = Post.objects.posts_ordenados_por_publicacion()
    template_name = "blog/post_list.html"
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ['autor', 'titulo', 'texto']
    success_url = reverse_lazy('post_list')
