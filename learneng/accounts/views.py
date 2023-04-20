from django.urls import reverse_lazy
from django.views import generic

from .forms import *


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


from django.shortcuts import render, redirect
from .forms import InfoForm


def visitors_info(request):
    error = ''
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ошибка'

    form = InfoForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'visitors_info.html', data)



