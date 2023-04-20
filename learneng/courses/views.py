from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lessons, Topics
from .forms import LessonsForm, TopicsForm
from django.views.generic import DetailView


def courses_home(request):
    lessons = Lessons.objects.all()
    topics = Topics.objects.all()
    return render(request, 'courses/courses_home.html', {'lessons': lessons, 'topics': topics})


class CoursesDetailView(DetailView):
    model = Lessons
    template_name = 'courses/details_view.html'
    context_object_name = 'lesson'


class TopicsDetailView(DetailView):
    model = Topics
    template_name = 'courses/topic_details.html'
    context_object_name = 'topic'


def create(request):
    error = ''
    if request.method == 'POST':
        form = LessonsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ошибка'

    form = LessonsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'courses/create.html', data)


def create_topics(request):
    error = ''
    if request.method == 'POST':
        form_topics = TopicsForm(request.POST)
        if form_topics.is_valid():
            form_topics.save()
            return redirect('home')
        else:
            error = 'ошибка'

    form_topics = TopicsForm()

    data = {
        'form_topics': form_topics,
        'error': error
    }

    return render(request, 'courses/create_topics.html', data)
