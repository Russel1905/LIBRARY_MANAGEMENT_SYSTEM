from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title

class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_membership = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.user.username} - {self.book.title}'
