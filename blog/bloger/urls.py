from django.contrib import admin
from django.urls import path
from bloger.views import mainpage, warface, gamescheats, warface_article, warface_comment, csgo, csgo_article, csgo_comment, rust, rust_comment, rust_article, fortnite, fortnite_article, fortnite_comment, anothergame_article, anothergame_comment, anothergame, soft_article, soft_comment, soft, programadd, programsadd, choosegame, anothergameadd, anothergameadds, warfaceadd, warfaceadds, rustadd, rustadds, fortniteadd, fortniteadds, csgoadd, csgoadds, profile 
urlpatterns = [
    path('main/', mainpage),
    path('profile/', profile),
    path('gamescheats/warface/', warface),
    path('gamescheats/csgo/', csgo),
    path('gamescheats/rust/', rust),
    path('gamescheats/anothergame/', anothergame),
    path('gamescheats/fortnite/', fortnite),
    path('programms/add/', programadd),
    path('programms/adds/', programsadd),
    path('gamescheats/', gamescheats),
    path('programms/', soft),
    path('gamescheats/add/', choosegame),
    path('gamescheats/anothergame/adds/', anothergameadds),
    path('gamescheats/warface/adds/', warfaceadds),
    path('gamescheats/rust/adds/', rustadds),
    path('gamescheats/fortnite/adds/', fortniteadds),
    path('gamescheats/csgo/adds/', csgoadds),
    path('gamescheats/warface/add/', warfaceadd),
    path('gamescheats/csgo/add/', csgoadd),
    path('gamescheats/fortnite/add/', fortniteadd),
    path('gamescheats/rust/add/', rustadd),
    path('gamescheats/anothergame/add/', anothergameadd),
    path('soft/<int:id>/', soft_article),
    path('gamescheats/warface/<int:id>/', warface_article),
    path('gamescheats/csgo/<int:id>/', csgo_article),
    path('gamescheats/warface/article/<int:id>/', warface_comment),
    path('gamescheats/csgo/article/<int:id>/', csgo_comment),
    path('gamescheats/rust/<int:id>/', rust_article),
    path('gamescheats/rust/article/<int:id>/', rust_comment),
    path('gamescheats/fortnite/<int:id>/', fortnite_article),
    path('gamescheats/fortnite/article/<int:id>/', fortnite_comment),
    path('gamescheats/anothergame/<int:id>/', anothergame_article),
    path('gamescheats/anothergame/article/<int:id>/', anothergame_comment),
    path('soft/article/<int:id>/', soft_comment),
]
    