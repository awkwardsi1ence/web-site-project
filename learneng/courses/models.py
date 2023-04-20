from django.db import models

from embed_video.fields import EmbedVideoField


class Lessons(models.Model):
    title = models.CharField('Название', max_length=100)
    url = EmbedVideoField('Видеоурок')
    full_text = models.TextField('Конспект урока')
    homework = models.TextField('Домашнее задание')
    added = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Topics(models.Model):
    title = models.CharField('Название', max_length=100)
    category = models.CharField('Категория', max_length=100)
    level = models.CharField('Уровень', max_length=50)
    full_text = models.TextField('Топик')
    added = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'




