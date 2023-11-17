from django.db import models
from django.utils import timezone
from ect.validators import rating_validator
#from django.contrib.auth.models import User

# Create your models here.
'''
Book
    -title 
    -author
    -publication date 
    -price
Author 
    -name 
    -birth_date
    -biography
Review
    -book 
    -reviewer_name
    -content 
    -rating(1:5)
'''

class Author(models.Model):
    name = models.CharField(max_length=30, blank= False, null = False)
    birth_date = models.DateField(null = False, blank= False)
    biography = models.TextField(max_length=1000, blank= True, null = False)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=20, blank=False, null = False)
    author = models.ForeignKey(Author, null =True, on_delete=models.CASCADE, related_name='book_author')
    publication_date = models.DateField(default= timezone.now)
    price = models.IntegerField()

    def __str__(self):
       return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name = 'review_book')
    reviewer_name = models.CharField(max_length=30, blank= False, null = False)
    content = models.TextField(max_length=5000, blank= True, null = False)
    rating = models.IntegerField(validators=[rating_validator])

    def __str__(self):
        return self.reviewer_name
