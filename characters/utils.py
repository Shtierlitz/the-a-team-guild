from django.db.models import Count

from .models import *
from django.core.cache import cache

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить персонажа", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class DataMixin:
        paginate_by = 5     # Пагинатор на 3 поста на странице (общий)

        def get_user_context(self, **kwargs):
                context = kwargs
                cats = cache.get('cats')
                if not cats:
                        cats = Category.objects.annotate(Count('character'))
                        cache.set('cats', cats, 60)

                user_menu = menu.copy()
                if not self.request.user.is_authenticated:
                        user_menu.pop(1)
                        # print(user_menu)

                context['menu'] = user_menu

                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0

                return context