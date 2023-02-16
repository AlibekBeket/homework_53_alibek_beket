from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from to_do_list.models import ToDo


def home_view(request: WSGIRequest):
    if request.POST:
        if request.POST.get('date') == "":
            date = None
        else:
            date = request.POST.get('date')
        to_do_add = {
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'date': date,
            'title': request.POST.get('title')
        }
        ToDo.objects.create(**to_do_add)
    to_do_list = ToDo.objects.all()
    context = {
        'to_do_list': to_do_list
    }
    return render(request, 'home_page.html', context=context)


def add_view(request: WSGIRequest):
    return render(request, 'add_page.html')


def detail_view(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    if to_do.date == None:
        to_do.date = ''
    return render(request, 'to_do_page.html', context={'to_do': to_do})
