from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import *
from .filters import PostFilter
from .forms import NewsForm, ArticlesForm


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = Post.objects.filter(type_post="NW")
        return context


class ArticlesList(ListView):
    model = Post
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Post.objects.filter(type_post="AR")
        return context


class SearchResults(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post'

    def get_queryset(self, *, object_list=None, **kwargs):
        return super().get_queryset().filter(type_post=Post.news)


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'articles_detail.html'
    context_object_name = 'post'

    def get_queryset(self, *, object_list=None, **kwargs):
        return super().get_queryset().filter(type_post=Post.article)


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        news_detail = form.save(commit=False)
        news_detail.type_post = 'NW'
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        news_detail = form.save(commit=False)
        news_detail.type_post = 'AR'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    ordering = '-time_in'
    template_name = 'news_update.html'


class ArticlesUpdate(UpdateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_update.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles')
