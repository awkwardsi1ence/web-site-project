from django import forms

from .models import Lessons, Topics
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, URLInput


class LessonsForm(ModelForm):
    class Meta:
        model = Lessons
        fields = ['title', 'url', 'full_text', 'homework', 'added']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название урока'
            }),
            "url": URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Видеоурок'
            }),
            "added": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Конспект урока'
            }),
            "homework": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Домашнее задание'
            })
        }


class TopicsForm(ModelForm):
    class Meta:
        model = Topics
        fields = ['title', 'category', 'level', 'full_text', 'added']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
            "level": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уровень'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Топик'
            }),
            "added": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            }),
        }

