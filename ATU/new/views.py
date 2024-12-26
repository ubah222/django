from django.shortcuts import render

from django.http import HttpResponse
from.models import book


def home (request):
    books = book.objects.all() # select * FROM book
    context = {
        'books': books
    }
    return render(request , 'index.html')

def about(request):
    return HttpResponse ('this is the about page')


