from django.db import models

from users.models import User

from django.template.defaultfilters import slugify

from django.shortcuts import reverse

# Create your models here.
class Discussion(models.Model):

    # Grade choices
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
        ('marketing', 'Marketing'),
        ('general', 'General'),
    )

    # Title of the question
    title = models.CharField(max_length=500, blank=False, verbose_name='Title')

    # Slug of the title
    slug = models.SlugField(verbose_name='Slug Fields', max_length=550)


    # Grade of Question
    grade = models.CharField(max_length=100, verbose_name='Class', blank=False, choices=grade_choices)

    # subject of question
    subject = models.CharField(max_length=100, verbose_name='Subject', blank=False, choices=subject_choices)

    # Question Detail
    detail = models.TextField(blank=False)

    # Views
    views = models.PositiveIntegerField(default=0)

    # answered or not
    answered_status = models.BooleanField(default=False, verbose_name='Is your question answered')

    # Question askedby
    askedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_questions')

    # time asked
    time = models.DateTimeField(auto_now_add=True)

    # Discussion Pinned
    pinned = models.BooleanField(verbose_name='Is discussion Pinned', default=False)
    
    def __str__(self):
        return self.title[:50]
    
    def increaseView(self):
        self.views = self.views + 1

    def changeanswerStatus(self):
        self.answered_status = not(self.answered_status)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Discussion, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'questiondetail', args = [
                self.pk,
                self.slug,
            ]
        )

class Answer(models.Model):

    # answer by
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer')

    # answer on which question
    answer_on = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='answers_ondiscussion')

    # time of answered
    time_posted = models.DateTimeField(auto_now_add=True)

    # answer
    answer = models.TextField(blank=False)

    def __str__(self):
        return f'{self.answer_on} by {self.answered_by}'