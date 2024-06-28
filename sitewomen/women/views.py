from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from women.forms import AddPostForm, UploadFileForm
from women.models import Women, Category, TagPost, UploadFiles
from django.views import View
from django.urls import reverse, reverse_lazy
from .utils import DataMixin


class WomenHome(DataMixin, ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Women.published.all().select_related('cat')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


class ShowPost(DataMixin, DetailView):
    template_name = 'women/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


def about(request):
    contact_list = Women.published.all()
    paginator = Paginator(contact_list, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'women/about.html',
                  {'title': 'О сайте', 'page_obj': page_obj})


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавление статьи'


class UpdatePage(DataMixin, UpdateView):
    model = Women
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактирование статьи'


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


class WomenCategory(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title=f'Категория - {cat.name}',
                                      cat_selected=cat.pk)


class WomenTags(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['posts'][0].tags.all()[0]
        return self.get_mixin_context(context,
                                      title=f'Тег - {tag.tag}',
                                      cat_selected=None)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


