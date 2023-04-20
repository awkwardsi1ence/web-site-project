from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ReviewForm


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def knowledge_base(request):
    return render(request, 'main/knowledge_base.html')


def test(request):
    return render(request, 'main/test.html')


def beginner(request):
    return render(request, 'main/levels/beginner.html')


def elementary(request):
    return render(request, 'main/levels/elementary.html')


def pre_intermediate(request):
    return render(request, 'main/levels/pre-intermediate.html')


def intermediate(request):
    return render(request, 'main/levels/intermediate.html')


def upper_intermediate(request):
    return render(request, 'main/levels/upper-intermediate.html')


def advanced(request):
    return render(request, 'main/levels/advanced.html')


def add_review(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse(form.errors.as_data())

    form = ReviewForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add_review.html', data)


