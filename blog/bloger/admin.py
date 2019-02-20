# -*- coding: utf-8 -*-
from django.contrib import admin
from bloger.models import Warface, Csgo, Rust, Fortnite, Anothergame, Soft, Comments_warface, Comments_csgo, Comments_rust, Comments_fortnite, Comments_anothergame, Comments_soft
cheatmodels = [Warface, Csgo, Rust, Fortnite, Anothergame, Comments_warface, Soft, Comments_csgo, Comments_rust, Comments_fortnite, Comments_anothergame, Comments_soft ]
admin.site.register(cheatmodels)
# Register your models here.
