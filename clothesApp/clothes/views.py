from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render

from clothes.models import clothes


def home(request):
    posts = clothes.objects.all()
    return render(request, 'clothes/home.html', {'posts': posts, 'title': 'Home page'})


def index(request):
    return render(request, 'clothes/index.html', {'title': 'Main page'})


def about(request):
    return render(request, 'clothes/about.html', {'title': 'About page'})


def categories(request, catId):
    return HttpResponse(f"Hello from Django <p>{catId}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>ERROR 404<br>Page not found</h1>')


def accessForbidden(request, exception):
    return HttpResponseForbidden('<h1>ERROR 403<br>Access forbidden</h1>')


def cantHandleQuery(request, exception):
    return HttpResponseBadRequest('<h1>ERROR 400<br>Bad request</h1>')


def errorServer(request):
    return HttpResponseServerError('<h1>ERROR 500<br>Server error, please try later</h1>')
