from django.contrib.sitemaps.views import index
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import DetailView, ListView, CreateView

from .models import PcType, PcBase
from .forms import PcAddForm
from .utils import DataMixin


class PcIndex(DataMixin, ListView):
    template_name = 'xmainsite/index.html'
    title_page = 'Главная страница'
    type_selected = 0

    def get_queryset(self):
        return PcBase.published.all().select_related('pc_type')


class PcAbout(DataMixin, DetailView):
    template_name = 'xmainsite/post.html'
    slug_url_kwarg = 'pc_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, pc_model=context['object'].pc_model)

    def get_object(self, queryset=None):
        return get_object_or_404(PcBase.published, pc_slug=self.kwargs[self.slug_url_kwarg])


class ShowPcType(DataMixin, ListView):
    template_name = 'xmainsite/index.html'
    context_object_name = 'pctypes'
    allow_empty = False

    def get_queryset(self):
        return PcBase.published.filter(pc_type__pctype_slug=self.kwargs['pctype_slug']).select_related("pc_type")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        typ = context['pctypes'][0].pc_type
        return self.get_mixin_context(context,
                                      title='Категория - ' + typ.pctype_name,
                                      typ_selected=typ.id,
                                      )


class PcAdd(DataMixin, CreateView):
    form_class = PcAddForm
    template_name = 'xmainsite/addpc.html'
    title_page = 'Добавление оборудования'


def about(request):
    return render(request, 'xmainsite/about.html',
                  {'title': 'О сайте'})


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

# class UpdatePage(DataMixin, UpdateView):
#     model = BasePC
#     fields = ['pc_model', 'pc_about', 'pc_photo', 'pc_pub', 'pc_type']
#     template_name = 'xmainsite/addpc.html'
#     success_url = reverse_lazy('index')
#     title_page = 'Редактирование статьи'


# class TagPostList(DataMixin, ListView):
#     template_name = 'women/index.html'
#     context_object_name = 'posts'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
#         return self.get_mixin_context(context, title='Тег: ' + tag.tag)
#
#     def get_queryset(self):
#         return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')
