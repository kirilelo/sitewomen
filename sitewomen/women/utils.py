menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {}
    paginate_by = 3

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context


class ExtraAttributeMixin:
    extra_context = {}
    category_id = None
    default_photo = None

    def __init__(self):
        if self.category_id:
            self.extra_context['category_id'] = self.category_id

        if self.default_photo:
            self.extra_context['default_photo'] = self.default_photo