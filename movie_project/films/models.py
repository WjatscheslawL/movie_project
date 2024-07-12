from django.db import models


# Create your models here.
class Films(models.Model):
    title = models.CharField('Название Фильма', max_length=50)
    autor = models.CharField('Автор', max_length=50)
    short_description = models.CharField('Краткое описание Фильма', max_length=200)
    text = models.TextField('OT3bIB')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'ФильмbI'
