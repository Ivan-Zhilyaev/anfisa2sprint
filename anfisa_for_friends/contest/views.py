from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContestForm
from .models import Contest

def proposal_create(request, pk=None):
    # Допишите функцию, чтобы она могла работать как на создание заявки,
    # так и на редактирование.
    # Если в запросе указан pk (если получен запрос на редактирование объекта):
    if pk is not None:
        # Получаем объект модели или выбрасываем 404 ошибку.
        instance = get_object_or_404(Contest, pk=pk)
    # Если в запросе не указан pk
    # (если получен запрос к странице создания записи):
    else:
        # Связывать форму с объектом не нужно, установим значение None.
        instance = None
    # Передаём в форму либо данные из запроса, либо None. 
    # В случае редактирования прикрепляем объект модели.
    form = ContestForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def delete_proposal(request, pk):
    # Допишите функцию для удаления заявок.
    # Получаем объект модели или выбрасываем 404 ошибку.
    instance = get_object_or_404(Contest, pk=pk)
    # В форму передаём только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = ContestForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос...
    if request.method == 'POST':
        # ...удаляем объект:
        instance.delete()
        # ...и переадресовываем пользователя на страницу со списком записей.
        return redirect('contest:accepted')
    # Если был получен GET-запрос — отображаем форму.
    return render(request, 'contest/form.html', context)


def accepted(request):
    bids = Contest.objects.all().order_by('id')
    context = {'bids': bids}
    return render(request, 'contest/proposal_accepted.html', context)
