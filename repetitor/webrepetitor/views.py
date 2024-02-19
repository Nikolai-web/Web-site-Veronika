from django.shortcuts import render
from .models import Bd, Rubric





def main_page(request):
    """Домашняя страница сайта"""
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
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










