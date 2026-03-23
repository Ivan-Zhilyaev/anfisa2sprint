# Импортируем класс TemplateView, чтобы унаследоваться от него.
from django.views.generic import TemplateView

from contest.models import Contest


class Description(TemplateView):
    # В атрибуте template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница.
    template_name = 'about/description.html'

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста из родительского метода.
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь ключ total_count;
        # значение ключа — число объектов модели Birthday.
        context['total_count'] = Contest.objects.count()
        # Возвращаем изменённый словарь контекста.
        return context
