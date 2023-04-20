from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Info(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    phone_number = PhoneNumberField('Контактный номер')
    email = models.EmailField('Эл. почта')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'




