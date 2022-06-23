from typing import Generic
from django.db.models.base import Model
from django import forms
from django.forms.models import _Fields
from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    Model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)


