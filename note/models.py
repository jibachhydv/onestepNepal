from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Note(models.Model):
    
    # Status Choice
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

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
        ('Bachelor', 'Bachelor'),
        ('General', 'General'),
    )

    # Subject Choice
    subject_choices = (
        ('physic', 'Physic'),
        ('chemistry', 'Chemistry'),
        ('botany', 'Botany'),
        ('zoology', 'Zoology'),
        ('math', 'Math'),
        ('english', 'English'),
        ('nepali', 'Nepali'),
        ('science', 'science'),
        ('social', 'Social'),
        ('eph', 'Environement,Population and Health'),
        ('Opt', 'Optional Math'),
        ('cs', 'Computer Science'),
        ('account', 'Account'),
        ('business', 'Business'),
        ('marketin', 'Marketing'),
        ('general', 'General'),
    )

    # title of the note
    title = models.CharField(max_length=250)

    # slug 
    slug = models.SlugField(max_length=255)

    # Author
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    # Content
    content = models.TextField()

    # publish
    publish = models.DateTimeField(default=timezone.now)

    # created
    created= models.DateTimeField(auto_now_add=True)

    # status
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    # Grade targeted
    grade = models.CharField(max_length=20, choices=grade_choices, default='General')

    # Subject Choice
    subject = models.CharField(max_length=25, choices=subject_choices, default='General')


    # Likes 
    likes = models.ManyToManyField(User, related_name='likedpost', blank=True)
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


    # Model Manager
    objects = models.Manager()
    published = PublishedManager() 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('note:note_detail', args=[
            self.pk,
            self.grade,
            self.subject,
            self.slug,

        ])
    
    # return number of likes
    def numberOfLikes(self):
        return self.likes.all().count()