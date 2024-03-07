from django.db import models


# Create your models here.
class Article(models.Model):
    hub_name = models.CharField('Название хаба', max_length=50)
    title = models.CharField('Название статьи', max_length=150)
    author_name = models.CharField('Имя автора', max_length=50)
    author_link = models.CharField('Сслыка на автора', max_length=75)
    datetime = models.CharField('Дата и время публикации', max_length=25)
    link = models.CharField('Ссылка на статью', max_length=75)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Hub(models.Model):
    hub_name = models.CharField('Название хаба', max_length=50)

    def __str__(self):
        return self.hub_name

    class Meta:
        verbose_name = 'Хаб'
        verbose_name_plural = 'Хабы'
