from django.db import models


class Reviews(models.Model):
    full_name = models.CharField('Полное имя', max_length=50)
    email = models.TextField('Электронная почта', max_length=50)
    photo = models.ImageField('Фотография пользователя')
    review_text = models.TextField('Отзыв пользователя')
    added = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
