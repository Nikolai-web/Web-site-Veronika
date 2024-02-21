from django.shortcuts import render, get_object_or_404
from .models import Bd, Rubric
from django.core.paginator import Paginator
from .forms import EmailPostForm




def main_page(request):
    """Домашняя страница сайта"""
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    # Постраничная разбивка
    paginator = Paginator(bbs, 1)
    page_nam = request.GET.get('page', 1)
    page = paginator.get_page(page_nam)
    context = {'rubrics': rubrics, 'page': page, 'bbs': page.object_list}
    return render(request, 'webrepetitor/main_page.html', context)



def rubric(request):
    """Информация о рубриках"""
    bbs = Bd.objects.order_by('id')
    rubric = Rubric.objects.order_by('id')
    context = {'bbs': bbs, 'rubrics': rubric}
    return render(request, 'webrepetitor/rubrici.html', context)


def haracteristic(request):
    """Характеристика"""
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'webrepetitor/haracteristic.html', context)


def price(request):
    """Цены"""
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'webrepetitor/price.html', context)


def predmet(request):
    """Предметы преподавания"""
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'webrepetitor/predmet.html', context)



def post_share(request, post_id):
    # Извлечь пост по id
    post = get_object_or_404(Bd, id=post_id, status=Bd.status.PUBLISHED)
    if request.method == 'POST':
        # Форма была передана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы прошли валидацию
            cd = form.cleaned_data
            # ....отправить электронное письмо
    else:
        form = EmailPostForm()
    return render(request, 'webrepetitor/share.html', {'post': post, 'form': form})





