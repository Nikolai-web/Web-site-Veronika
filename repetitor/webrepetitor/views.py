from django.shortcuts import render, get_object_or_404
from .models import Bd, Rubric
from django.core.paginator import Paginator
from .forms import EmailPostForm
from django.core.mail import send_mail



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
    posts = Bd.published.all()
    return render(request, 'webrepetitor/rubrici.html', {'posts': posts})



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



def post_share(request):
    # Извлечь пост по id
    post = Bd.published.all()
    sent = False
    if request.method == 'POST':
        # Форма была передана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы прошли валидацию
            cd = form.cleaned_data
            # ....отправить электронное письмо
            subject = f"{cd['name']} recommends you read"\
            f" {post.title}"

            message = f"Read {post.title} \n\n" \
            f" {cd['name']}\ comments: {cd['comments']}"

            send_mail(subject, message, 'spriteverdar777@gmail.com',
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'webrepetitor/share.html', {'post': post, 'form': form, 'sent': sent})




def post_detail(request, id):
    post = get_object_or_404(Bd, id=id, status=Bd.Status.PUBLISHED)
    return render(request, 'webrepetitor/detail.html', {'post': post})



