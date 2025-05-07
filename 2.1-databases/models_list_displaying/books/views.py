from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all().order_by('pub_date')
    context = {"books": book_objects,}
    return render(request, template, context)

def books_view_date(request, pub_date):
    
    template = 'books/books_list.html'
    book_objects  = Book.objects.filter(pub_date = pub_date)
    pub_date_prev = Book.objects.filter(pub_date__lt = pub_date).order_by('pub_date').last()  
    pub_date_next = Book.objects.filter(pub_date__gt = pub_date).order_by('pub_date').first()    
    # pub_date_next = Book.objects.extra(where=['pub_date' > pub_date]).order_by('pub_date').first()
       
    
    context = {"books": book_objects,
               "prev": pub_date_prev,
               "next": pub_date_next,}
    return render(request, template, context)
