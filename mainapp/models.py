from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Option(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Answer(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=256)
    is_right = models.BooleanField(default=True)

    def __str__(self):
        return self.answer


class Question(models.Model):
    QUESTION_TYPES = (
        ('1', 'Ответ текстом'),
        ('2', 'Ответ с выбором одного варианта'),
        ('3', 'Ответ с выбором нескольких вариантов')
    )

    article = models.TextField()
    type = models.CharField(max_length=1, choices=QUESTION_TYPES, default=1)
    options = models.ManyToManyField(Option, blank=True)
    right_answer = models.CharField(max_length=256, null=True, blank=True)
    answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return self.article


class Test(models.Model):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField(Question)
    amount_of_questions = models.PositiveSmallIntegerField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
