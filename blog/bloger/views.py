# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from bloger.models import Warface, Csgo, Rust, Fortnite, Anothergame, Soft, Comments_warface, Comments_csgo, Comments_rust, Comments_fortnite, Comments_anothergame, Comments_soft
from bloger.forms import CommentForm_warface, CommentForm_csgo, CommentForm_rust, CommentForm_fortnite, CommentForm_anothergame, Addprogram, CommentForm_soft, Addwarface, Addcsgo, Addrust, Addfortnite, Addanothergame
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from social_core.exceptions import AuthForbidden

def mainpage(request):
    return render_to_response ('mainpage.html', {'user': auth.get_user(request)})
def gamescheats(request):
    return render_to_response ('gamescheats.html', {'user': auth.get_user(request)}) #vkladka cheatov 
def profile(request):
    args = {}
    args['user'] = auth.get_user(request)
    return render_to_response ('profile.html', args)
def warface(request):
    contact_list = Warface.objects.all().order_by('-warface_date')
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'warfaceblog.html', {'warface_articles': contact_list, 'items': items})
def rust(request):
    contact_list = Rust.objects.all().order_by('-rust_date')
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'rustblog.html', {'rust_articles': contact_list, 'items': items})
def csgo(request):
    contact_list = Csgo.objects.all().order_by('-csgo_date')
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'csgoblog.html', {'csgo_articles': contact_list, 'items': items})
def fortnite(request):
    contact_list = Fortnite.objects.all().order_by('-fortnite_date')
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'fortniteblog.html', {'fortnite_articles': contact_list, 'items': items})
def anothergame(request):
    contact_list = Anothergame.objects.all().order_by('-anothergame_date')
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'anothergameblog.html', {'anothergame_articles': contact_list, 'items': items})
def soft(request):
    contact_list = Soft.objects.all().order_by('-soft_date')
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'softblog.html', {'soft_articles': contact_list, 'items': items})

def warface_article(request, id): #skript kagdoy statii
    form = CommentForm_warface()
    args = {}
    args.update(csrf(request))
    args['articles'] = Warface.objects.get(id = id)
    args['comment'] = Comments_warface.objects.filter(comment_warface_id = id)
    args['form'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('warface_article.html', args)
def warface_comment(request, id,):
    if request.method == 'POST':
        forms = CommentForm_warface(request.POST)
        if forms.is_valid():
            comment = forms.save(commit = False)
            comment.comment_warface_id = id
            comment.comment_warface_author = request.user
            comment.save()
    return redirect ('/cybercheats/gamescheats/warface/%s/' % id)
    
def csgo_article(request, id): 
    form = CommentForm_csgo()
    args = {}
    args.update(csrf(request))
    args['articles'] = Csgo.objects.get(id = id)
    args['comment'] = Comments_csgo.objects.all()
    args['form'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('csgo_article.html', args)
def csgo_comment(request, id,):
    if request.method == 'POST':
        forms = CommentForm_csgo(request.POST)
        if forms.is_valid():
            comment = forms.save(commit = False)
            comment.comment_csgo_id = id
            comment.comment_csgo_author = request.user
            comment.save()
    return redirect ('/cybercheats/gamescheats/csgo/%s/' % id)

def rust_article(request, id): #skript kagdoy statii
    form = CommentForm_rust()
    args = {}
    args.update(csrf(request))
    args['articles'] = Rust.objects.get(id = id)
    args['comment'] = Comments_rust.objects.all()
    args['form'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('rust_article.html', args)
def rust_comment(request, id,):
    if request.method == 'POST':
        forms = CommentForm_rust(request.POST)
        if forms.is_valid():
            comment = forms.save(commit = False)
            comment.comment_rust_id = id
            comment.comment_rust_author = request.user
            comment.save()
    return redirect ('/cybercheats/gamescheats/rust/%s/' % id)

def fortnite_article(request, id): #skript kagdoy statii
    form = CommentForm_fortnite()
    args = {}
    args.update(csrf(request))
    args['articles'] = Fortnite.objects.get(id = id)
    args['comment'] = Comments_fortnite.objects.filter(comment_fortnite_id = id)
    args['form'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('fortnite_article.html', args)
def fortnite_comment(request, id,):
    if request.method == 'POST':
        forms = CommentForm_fortnite(request.POST)
        if forms.is_valid():
            comment = forms.save(commit = False)
            comment.comment_fortnite_id = id
            comment.comment_fortnite_author = request.user
            comment.save()
    return redirect ('/cybercheats/gamescheats/fortnite/%s/' % id)

def anothergame_article(request, id): #skript kagdoy statii
    form = CommentForm_anothergame()
    args = {}
    args.update(csrf(request))
    args['articles'] = Anothergame.objects.get(id = id)
    args['comment'] = Comments_anothergame.objects.filter(comment_anothergame_id = id)
    args['form'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('anothergame_article.html', args)
def anothergame_comment(request, id,):
    if request.method == 'POST':
        forms = CommentForm_anothergame(request.POST)
        if forms.is_valid():
            comment = forms.save(commit = False)
            comment.comment_anothergame_id = id
            comment.comment_anothergame_author = request.user
            comment.save()
    return redirect ('/cybercheats/gamescheats/anothergame/%s/' % id)

def soft_article(request, id): #skript kagdoy statii
    form = CommentForm_soft()
    args = {}
    args.update(csrf(request))
    args['articles'] = Soft.objects.get(id = id)
    args['comment'] = Comments_soft.objects.filter(comment_soft_id = id)
    args['form'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('soft_article.html', args)
def soft_comment(request, id):
    if request.method == 'POST':
        forms = CommentForm_soft(request.POST)
        if forms.is_valid():
            comment = forms.save(commit = False)
            comment.comment_soft_id = id
            comment.comment_soft_author = request.user
            comment.save()
    return redirect ('/cybercheats/soft/%s/' % id)

def programadd (request):
    form = Addprogram()
    args = {}
    args.update(csrf(request))
    args['forms'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('addprogram.html', args)
def programsadd (request):
    if request.method == 'POST':
        forms = Addprogram(request.POST)
        if forms.is_valid():
            save = forms.save(commit=False)
            save.soft_author = request.user
            save.save()
    return redirect ('/cybercheats/programms/')

def choosegame(request):
    return render_to_response('choosegame.html', {'user': auth.get_user(request)})
    
def warfaceadd(request):
    args = {}
    form = Addwarface()
    args.update(csrf(request))
    args['forms'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('addwarface.html', args)
def warfaceadds(request):
    if request.method == 'POST':
        forms = Addwarface(request.POST)
        if forms.is_valid():
            item = forms.save(commit=False)
            item.warface_author = request.user
            item.save()
    return redirect('/cybercheats/gamescheats/warface/')

def csgoadd(request):
    args = {}
    form = Addcsgo()
    args.update(csrf(request))
    args['forms'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('addcsgo.html', args)
def csgoadds(request):
    if request.method == 'POST':
        forms = Addcsgo(request.POST)
        if forms.is_valid():
            item = forms.save(commit=False)
            item.csgo_author = request.user
            item.save()
    return redirect('/cybercheats/gamescheats/csgo/')

def rustadd(request):
    args = {}
    form = Addrust()
    args.update(csrf(request))
    args['forms'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('addrust.html', args)
def rustadds(request):
    if request.method == 'POST':
        forms = Addrust(request.POST)
        if forms.is_valid():
            item = forms.save(commit=False)
            item.rust_author = request.user
            item.save()
    return redirect('/cybercheats/gamescheats/rust/')

def fortniteadd(request):
    args = {}
    form = Addfortnite()
    args.update(csrf(request))
    args['forms'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('addfortnite.html', args)
def fortniteadds(request):
    if request.method == 'POST':
        forms = Addfortnite(request.POST)
        if forms.is_valid():
            item = forms.save(commit=False)
            item.fortnite_author = request.user
            item.save()
    return redirect('/cybercheats/gamescheats/fortnite/')

def anothergameadd(request):
    args = {}
    form = Addanothergame()
    args.update(csrf(request))
    args['forms'] = form
    args['user'] = auth.get_user(request)
    return render_to_response ('addanothergame.html', args)
def anothergameadds(request):
    if request.method == 'POST':
        forms = Addanothergame(request.POST)
        if forms.is_valid():
            item = forms.save(commit=False)
            item.anothergame_author = request.user
            item.save()
    return redirect('/cybercheats/gamescheats/anothergame/')