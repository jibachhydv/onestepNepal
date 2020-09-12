from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


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
    content = models.TextField(blank=False)

    # publish
    publish = models.DateTimeField(default=timezone.now)

    # created
    created= models.DateTimeField(auto_now_add=True)

    # status
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    # Grade targeted
    grade = models.CharField(max_length=20, choices=grade_choices)

    # Subject Choice
    subject = models.CharField(max_length=25, choices=subject_choices)

    # Views Count
    views = models.PositiveIntegerField(blank=False, default=0)


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
        return reverse('notedetail', args=[
            self.pk,
            self.slug,
        ])
    
    # return number of likes
    def numberOfLikes(self):
        return self.likes.all().count()
    
    def increaseView(self):
        self.views = self.views + 1


class Comment(models.Model):

    # comment on which post
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    # Comment
    comment = models.TextField()

    # Time
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:50]