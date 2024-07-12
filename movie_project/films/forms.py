from .models import Films
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class News_postForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'autor', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Hазвания фильма'}),
            'autor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
        }
