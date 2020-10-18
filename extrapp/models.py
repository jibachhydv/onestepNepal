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
    coverImage = models.ImageField(verbose_name='Book Cover Image', upload_to='readnepal', null=True)

    # Date
    date = models.DateField()

    # Reader
    reader = models.ManyToManyField(to=User, blank=True, related_name='books')

    # isItCurrentBook
    isItCurrentBook = models.BooleanField(verbose_name='Is this a Book of Month', default=False)

    def __str__(self):
        return f"{self.name} {self.date}"

class Participiant(models.Model):

    # participiant Name
    reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reader')

    # Book Name
    bookName = models.ForeignKey(CurrentBook, on_delete=models.CASCADE, related_name='bookName')

    # Date 
    dateStarted = models.DateField(auto_now_add=True)

    # Mark as done
    doneReading = models.BooleanField(verbose_name="Done Reading Book?", default=False)

    class Meta:
        unique_together = ('reader', 'bookName')

    def __str__(self):
        return f"{self.reader.email} is reading {self.bookName.name}"