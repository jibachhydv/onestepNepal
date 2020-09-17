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

    # Participated By
    participatedBy = models.ManyToManyField(User, related_name='participatedBy')

    # Date
    date = models.DateField()

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

