from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.core.exceptions import ValidationError


class User(AbstractUser):
    # Grade Choices
    grade_choices = (
        ('1-5', 'One to Five'),
        ('6', 'Six'),
        ('7', 'Seven'),
        ('8', 'Eight'),
        ('9', 'Nine'),
        ('10', 'Ten'),
        ('11', 'Eleven'),
        ('12', 'Twelve'),
        ('HA', 'Health Assistant'),
        ('Diploma in Engineering', 'Diploma'),
        ('Bachelor in CSIT', 'Bachelor in CSIT'),
        ('Bachelor in Agriculture', 'Bachelor in Agriculture'),
        ('Diploma in Agriculture', 'Diploma in Agriculture'),
        ('Bachelor in Engineering', 'Bachelor in Engineering'),
        ('Bachelor in Education', 'Bachelor in Education'),
        ('Bachelor in Commerce', 'Bachelor in Commerce'),
        ('BSC Nursing', 'Bachelor in Nursing'),
        ('Bachelor in CSIT', 'Bachelor in CSIT'),
        ('General', 'General'),
    )

    # Faculty Choosen
    faculty = (
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Art', 'Art'),
        ('Medicine', 'Medicine'),
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
    )

    first_name = models.CharField(
        blank=False,
        max_length=100)

    last_name = models.CharField(
        blank=False,
        max_length=100)

    email = models.EmailField(unique=True,
                              blank=False,
                              max_length=255)

    username = models.CharField(max_length=30,
                                unique=False)

    hobby = models.CharField(max_length=200,
                             blank=True)

    favorite_quotes = models.CharField(max_length=200,
                                       blank=True)

    photo = models.ImageField(upload_to='profile',
                              blank=True,
                              null=True)

    grade = models.CharField(
        max_length=200,
        choices=grade_choices,
        blank=True
    )

    schoolType = models.CharField(max_length=200, choices=faculty, blank=True)

    schoolName = models.CharField(max_length=100,
                                  blank=True)

    address = models.CharField(max_length=200,
                               blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.first_name} + {self.last_name} +({self.email})"

    def get_absolute_url(self):
        return reverse('profile', args=[
            self.pk,
        ])


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def clean(self):
        if self.follower == self.following:
            raise ValidationError("One Cannot follow themselves")

    def __str__(self):
        return '%s follows %s' % (self.follower, self.following)

