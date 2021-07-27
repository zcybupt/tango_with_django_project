from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse('<p>Rango says here is the about page.</p>'
                        '<a href="/rango/">Index</a>')
