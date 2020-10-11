from django.db import models

from users.models import User

# Create your models here.
class CurrentBook(models.Model):

    # Name of Book
    name = models.CharField(max_length=200, verbose_name='Book Name')

    # Writer of Book
    writer = models.CharField(max_length=200, verbose_name='Book Writer')

    # Summary of the Book
    summary = models.TextField(max_length=1000)

    # CoverImage of the Book
    coverImage = models.ImageField(verbose_name='Book Cover Image', upload_to='readnepal')

    # Date
    date = models.DateField()

    # isItCurrentBook
    isItCurrentBook = models.BooleanField(verbose_name='Is this a Book of Month')

    def __str__(self):
        return self.name
    

    

class OtherBook(models.Model):

    # Book Name
    name = models.CharField(verbose_name='Book Name', max_length=200)

    # participated By
    participatedBy = models.ForeignKey(User, related_name='participatedByOther', on_delete=models.CASCADE)

    # status
    status = models.BooleanField(verbose_name='Do You Completed Reading?')

    # month
    status = models.DateField()

    def __str__(self):
        return f'{self.participatedBy} is reading {self.name}'

class ReadNepalParticipant(models.Model):
    
    # Reader Name
    readerName = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookreader')

    # Date Joined
    dateJoined = models.DateTimeField(verbose_name='Reader Joined Date', auto_now=True)

    # Book Name
    bookName = models.ForeignKey(CurrentBook, on_delete=models.CASCADE, related_name='booksName')

    # Complete Reading
    readingStatus = models.BooleanField(verbose_name='Have you completed Reading')

    def __str__(self):
        return f"{self.readerName} is reading {self.bookName}"

