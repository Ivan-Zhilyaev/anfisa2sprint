from django.shortcuts import render

from .forms import ContestForm
from .models import Contest

def proposal_create(request):
    form = ContestForm(request.POST or None)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def accepted(request):
    bids = Contest.objects.all().order_by('id')
    context = {'bids': bids}
    return render(request, 'contest/proposal_accepted.html', context)
