from django.db import models
from django.urls import reverse




class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Bd.Status.PUBLISHED)


class Bd(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PF', 'Опубликовано'
    # Заголовок
    title = models.CharField(max_length=250)
    # Короткая метка
    slag = models.SlugField(max_length=250)
    # Сам текст, описание информации
    content = models.TextField()
    # Цена, вещественное число
    price = models.FloatField()
    # Присваиваем текущую дату и время записи. Индекс для сортировки даты по убыванию.
    published_time = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    # Опубликованные рубрики
    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name='Рубрика')
    objects = models.Manager()
    # Менеджер, который позволяет извлекать посты
    published = PublishedManager()

    def __str__(self):
        return f'{self.title} - {self.content}'

    def get_absolute_url(self):
        return reverse('webrepetitor:main_page', args=[self.id])


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


