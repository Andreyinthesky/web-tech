#coding: utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')
    
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default="", max_length=1024) #заголовок вопроса
    text = models.TextField(default="") #полный текст вопроса
    added_at = models.DateTimeField(blank=True, auto_now_add=True) #дата добавления вопроса
    rating = models.IntegerField(default=0) #рейтинг вопроса (число)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #автор вопроса
    likes = models.ManyToManyField(User, related_name='question_like_user') #список пользователей, поставивших "лайк"
    
    def __str__(self):
        return self.title

    def get_url(self):
        return "/question/{}/".format(self.id)

    

    
class Answer(models.Model):
    text =  models.TextField(default="") #текст ответа
    added_at = models.DateTimeField(blank=True, auto_now_add=True) # дата добавления ответа
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL) # вопрос, к которому относится ответ
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # автор ответа
    
    def __str__(self):
        return self.text
