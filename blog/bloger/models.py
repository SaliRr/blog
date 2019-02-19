# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Warface(models.Model):
    warface_title = models.CharField(max_length = 30, verbose_name='Заголовок статьи')
    warface_date = models.DateTimeField(auto_now=True)
    warface_body = models.TextField(verbose_name = 'Описание программы')
    warface_cheatlink = models.CharField(max_length = 50, verbose_name='Ссылка на чит')
    warface_author = models.ForeignKey(User, on_delete=models.CASCADE,)
class Csgo(models.Model):
    csgo_title = models.CharField(max_length = 30, verbose_name='Заголовок статьи')
    csgo_date = models.DateTimeField(auto_now=True)
    csgo_body = models.TextField(verbose_name = 'Описание программы')
    csgo_cheatlink = models.CharField(max_length = 50, verbose_name='Ссылка на чит')
    csgo_author = models.ForeignKey(User, on_delete=models.CASCADE,)
class Rust(models.Model):
    rust_title = models.CharField(max_length = 30, verbose_name='Заголовок статьи')
    rust_date = models.DateTimeField(auto_now=True)
    rust_body = models.TextField(verbose_name = 'Описание программы')
    rust_cheatlink = models.CharField(max_length = 50, verbose_name='Ссылка на чит')
    rust_author = models.ForeignKey(User, on_delete=models.CASCADE,)
class Fortnite(models.Model):
    fortnite_title = models.CharField(max_length = 30, verbose_name='Заголовок статьи')
    fortnite_date = models.DateTimeField(auto_now=True)
    fortnite_body = models.TextField(verbose_name = 'Описание программы')
    fortnite_cheatlink = models.CharField(max_length = 50, verbose_name='Ссылка на чит')
    fortnite_author = models.ForeignKey(User, on_delete=models.CASCADE,)
class Anothergame(models.Model):
    anothergame_title = models.CharField(max_length = 30, verbose_name='Заголовок статьи')
    anothergame_date = models.DateTimeField(auto_now=True)
    anothergame_body = models.TextField(verbose_name = 'Описание программы')
    anothergame_cheatlink = models.CharField(max_length = 50, verbose_name='Ссылка на чит')
    anothergame_author = models.ForeignKey(User, on_delete=models.CASCADE,)
class Soft(models.Model):
    soft_title = models.CharField(max_length = 30, verbose_name='Заголовок статьи')
    soft_date = models.DateTimeField(auto_now=True,)
    soft_body = models.TextField(verbose_name = 'Описание программы')
    soft_cheatlink = models.CharField(max_length = 50, verbose_name='Ссылка на чит')
    soft_author = models.ForeignKey(User, on_delete=models.CASCADE,)

class Comments_warface(models.Model):
    class Meta:
        db_table = 'comments_warface'
    
    comment_text = models.TextField(verbose_name='комментарий')
    comment_warface = models.ForeignKey('Warface', on_delete=models.CASCADE,)
    comment_date = models.DateTimeField(auto_now=True)
    comment_warface_author = models.ForeignKey(User, on_delete=models.CASCADE,)

class Comments_csgo(models.Model):
    class Meta:
        db_table = 'comments_csgo'
    
    comment_text = models.TextField(verbose_name='комментарий')
    comment_csgo = models.ForeignKey('Csgo', on_delete=models.CASCADE,)
    comment_csgo_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment_date = models.DateTimeField(auto_now=True)
class Comments_rust(models.Model):
    class Meta:
        db_table = 'comments_rust'
    
    comment_text = models.TextField(verbose_name='комментарий')
    comment_rust = models.ForeignKey('Rust', on_delete=models.CASCADE,)
    comment_rust_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment_date = models.DateTimeField(auto_now=True)
class Comments_fortnite(models.Model):
    class Meta:
        db_table = 'comments_fortnite'
    
    comment_text = models.TextField(verbose_name='комментарий')
    comment_fortnite = models.ForeignKey('Fortnite', on_delete=models.CASCADE,)
    comment_fortnite_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment_date = models.DateTimeField(auto_now=True)
class Comments_anothergame(models.Model):
    class Meta:
        db_table = 'comments_anothergame'
    
    comment_text = models.TextField(verbose_name='комментарий')
    comment_anothergame = models.ForeignKey('Anothergame', on_delete=models.CASCADE,)
    comment_anothergame_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment_date = models.DateTimeField(auto_now=True)
class Comments_soft(models.Model):
    class Meta:
        db_table = 'comments_soft'
    
    comment_text = models.TextField(verbose_name='комментарий')
    comment_soft = models.ForeignKey('Soft', on_delete=models.CASCADE,)
    comment_soft_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment_date = models.DateTimeField(auto_now=True)
    
# Create your models here.
