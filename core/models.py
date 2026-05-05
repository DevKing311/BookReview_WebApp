from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Writer(models.Model):
    gender_choice= [('male','Male'),('others','Others'),('female','Female')]
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,choices=gender_choice)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='writers_pics/')
    
    def __str__(self):
        
        return f"{self.name}"

class Books(models.Model):
    title=models.CharField(max_length=200)
    Summary= models.TextField()
    book_cover = models.ImageField(upload_to='book_covers/')
    pub_year =models.PositiveBigIntegerField()
    price = models.FloatField()
    genre = models.CharField(max_length=150)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    #the Writer is the model name you want to refrence to
    def __str__(self):
        return f"{self.title}"
    
    #note since you use that auto add you will not see it in the admin but you will see in the database 
   
class Review(models.Model):
    name = models.CharField(max_length=150, blank=True ,null=True)
    rating = models.PositiveBigIntegerField()
    comment=models.TextField()
    book= models.ForeignKey(Books, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"

class NewsAndEvent(models.Model):
    cover = models.ImageField(upload_to='news_cover')
    news_title = models.CharField(max_length=250)
    news_content = models.TextField()
    created_at = models.DateField (auto_now_add=True)
    def __str__(self):
        return f"{self.news_title}"