from django.urls import path
from core.views import * 

urlpatterns =[
    path('', index, name = 'homepage'),
    path('news',news, name = 'news'),
    path('books',books, name = 'book_link'),
    path('books/<id>', books_details, name = 'book-detail'),
    path('writers',writers, name = 'writers_link'),
    path('register',Register, name = 'register'),
    path('login',login_view, name = 'login'),
    path('logout',signout, name = 'logout'),
    
]
