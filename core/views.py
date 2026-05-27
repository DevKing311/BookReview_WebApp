from django.shortcuts import render , redirect
from core.models import *
from django.db.models import Q
from random import choice
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    all_books = Books.objects.all()
    top_two_news = NewsAndEvent.objects.order_by('created_at')[:2]
    #normal python slicing to get the last two 
    random_book = choice(all_books)
    ctx = {'random_book':random_book,
           'top_two_news':top_two_news}
    return render(request,'index.html',ctx)

def news (request):
    return render(request,'news.html')
@login_required(login_url='login')
def books(request):
    book_title = request.GET.get('book_title')
    if book_title is not None:
        all_books = Books.objects.filter( Q(title__icontains= book_title)|Q(genre__icontains= book_title) )
    else:
        all_books = Books.objects.all()
    ctx = {"bookss": all_books}
    return render(request,'books.html', ctx)


def writers(request):
    writers= Writer.objects.all()
    ctx = {"writers":writers}
    return render(request,'writers.html', ctx)


def books_details(request, id):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        review_comment = request.POST.get('comment')
        review_rating = request.POST.get('rating')

        retrived_book = Books.objects.get(id = id)
        Review.objects.create(name = full_name,comment= review_comment,
        rating=review_rating,book=retrived_book)

        return redirect(f'/books/{id}')

    bookz = Books.objects.get(id = id)
    book_reviews = Review.objects.filter(book = bookz)

    ctx = {"bookz":bookz,"book_reviews":book_reviews }
          
    return render(request,'books_details.html', ctx)

def login_view(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('book_link')   
        else:
            return render(request, 'login.html', {
                'error': 'Wrong username or password'
            })
    return render(request,'login.html')

def Register(request):
    if request.method=='POST':
         fname = request.POST.get('first_name')
         lname = request.POST.get('last_name')
         email = request.POST.get('email')
         username = request.POST.get('username')
         password = request.POST.get('password')
         cpassword = request.POST.get('cpassword')

         if password != cpassword:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

         User.objects.create_user(first_name=fname,last_name=lname,
         email=email,username=username,password=password)

         messages.success(request, f"Account created successfully! Username: {username}")
         return redirect('login')
    return render(request,'register.html')
def signout(request):

    logout(request)
    return redirect('homepage')
#note we use signout because django has a function named logout to prevent clash

