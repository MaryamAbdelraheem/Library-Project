from rest_framework import serializers
from .models import Author, Book, Review

class AuthorSerializers(serializers.ModelSerializers):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializers(serializers.ModelSerializers):
    class Meta:
        model = Book
        fields = '__all__'
    
class ReviewSerializers(serializers.ModelSerializers):
    class Meta:
        model = Review
        fields = '__all__'
