# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from bloger.models import Comments_warface, Comments_csgo, Comments_rust, Comments_fortnite, Comments_anothergame, Comments_soft, Soft, Warface, Csgo, Rust, Fortnite, Anothergame 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Addprogram(ModelForm):
    class Meta:
        model = Soft
        fields = ('soft_title', 'soft_body', 'soft_cheatlink', )
class Addwarface(ModelForm):
    class Meta:
        model = Warface
        fields = ('warface_title', 'warface_body', 'warface_cheatlink')
class Addcsgo(ModelForm):
    class Meta:
        model = Csgo
        fields = ('csgo_title', 'csgo_body', 'csgo_cheatlink')
class Addrust(ModelForm):
    class Meta:
        model = Rust
        fields = ('rust_title', 'rust_body', 'rust_cheatlink')
class Addfortnite(ModelForm):
    class Meta:
        model = Fortnite
        fields = ('fortnite_title', 'fortnite_body', 'fortnite_cheatlink')
class Addanothergame(ModelForm):
    class Meta:
        model = Anothergame
        fields = ('anothergame_title', 'anothergame_body', 'anothergame_cheatlink')
class CommentForm_warface(ModelForm):
    class Meta:
        model = Comments_warface 
        fields = ('comment_text',)
class CommentForm_csgo(ModelForm):
    class Meta:
        model = Comments_csgo 
        fields = ('comment_text',)
class CommentForm_rust(ModelForm):
    class Meta:
        model = Comments_rust 
        fields = ('comment_text',)
class CommentForm_fortnite(ModelForm):
    class Meta:
        model = Comments_fortnite 
        fields = ('comment_text',)
class CommentForm_anothergame (ModelForm):
    class Meta:
        model = Comments_anothergame 
        fields = ('comment_text',)
class CommentForm_soft (ModelForm):
    class Meta:
        model = Comments_soft 
        fields = ('comment_text',)
        
