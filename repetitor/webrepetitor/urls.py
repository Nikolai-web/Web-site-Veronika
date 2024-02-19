from django.urls import path
from . import views

app_name = 'webrepetitor'

urlpatterns = [
    # Домашняя страница
    path('', views.main_page, name='main_page'),
    # Страница со списком информации о репетиторе
    path('rubric', views.rubric, name='rubric'),
    path('haracteristic', views.haracteristic, name='haracteristic'),
    path('price', views.price, name='price'),
    path('predmet', views.predmet, name='predmet')

]