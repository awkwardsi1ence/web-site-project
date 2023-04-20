from .models import Reviews
from django.forms import ModelForm, TextInput, EmailInput, FileInput, Textarea


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['full_name', 'photo', 'email', 'review_text']

        widgets = {
            "full_name": TextInput(attrs={
                'class': 'form-control',
            }),
            "photo": FileInput(attrs={
                'class': 'form-control',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
            }),
            "review_text": Textarea(attrs={
                'class': 'form-control',
            }),
        }




