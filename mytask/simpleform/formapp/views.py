from django.shortcuts import render,redirect # redirectを追記

# Create your views here.

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel
from django.http import Http404
from . import models

class ListClass(ListView):
    template_name = 'list.html'
    model = PostModel

class FormClass(CreateView):
    template_name = 'form.html'
    model = PostModel
    fields = ('title','memo')
    success_url = reverse_lazy('list')

def edit(request,pk):
    template_name = "blog/edit.html"
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    if request.POST == "POST":
        article.title = request.POST["title"]
        article.text = request.POST["text"]
        article.save()
    context = {"article": article}
    return render(request, template_name, context)
    