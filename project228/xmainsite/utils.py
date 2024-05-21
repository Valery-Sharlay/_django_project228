menu_top = [
    {'title': "Добавить...", 'url_name': 'pcadd'},
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Авторизация", 'url_name': 'login'},
    ]


class DataMixin:
    title_page = None
    pctype_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            # self.extra_context['pc_name'] = self.title_page
            self.extra_context['title'] = self.title_page

        if self.pctype_selected is not None:
            self.extra_context['pctype_selected'] = self.pctype_selected

        if 'menu_top' not in self.extra_context:
            self.extra_context['menu_top'] = menu_top

    def get_mixin_context(self, context, **kwargs):
        context['menu_top'] = menu_top
        context['pctype_selected'] = None
        context.update(kwargs)
        return context
