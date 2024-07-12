from django.shortcuts import render, redirect
from .models import Films
from .forms import News_postForm
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'films/films_info.html')


def films(request):
    films = Films.objects.all()
    return render(request, 'films/films_info.html', {'films': films})


def create_new_film(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('films/films_info.html')
        else:
            error = "Данные были заполнены некорректно"
    form = News_postForm()
    return render(request, 'films/add_new_film.html', {'form': form, 'error': error})


