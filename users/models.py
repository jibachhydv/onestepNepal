from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.core.exceptions import ValidationError


class User(AbstractUser):
    # Grade Choices
    grade_choices = (
        ('One to Five', 'One to Five'),
        ('Six', 'Six'),
        ('Seven', 'Seven'),

        ('Eight', 'Eight'),
        ('Nine', 'Nine'),
        ('Ten', 'Ten'),

        ('Eleven', 'Eleven'),
        ('Twelve', 'Twelve'),

        ('HA', 'Health Assitant'),
        ('Staff Nurse', 'Staff Nurse'),

        ('Diploma in Agriculture', 'Diploma in Agriculture'),
        ('Diploma in Engineering', 'Diploma in Engineering'),



        ('Bachelor in CSIT', 'Bachelor in CSIT'),
        ('BSC Nursing', 'BSC Nursing'),
        ('Bachelor in Education', 'Bachelor in Education'),
        ('Bachelor in Engineering', 'Bachelor in Engineering'),
        ('BBS', 'BBS'),
        ('BBA', 'BBA'),
        ('MBBS', 'MBBS'),
        
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
                              default='../static/images/Flag_of_Nepal.png'
                              )

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
    
    def fullname(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


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

