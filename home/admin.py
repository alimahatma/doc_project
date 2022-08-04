from re import A
from wsgiref.validate import WriteWrapper
from django.contrib import admin

from .models import Category, Autor, Artikel

class TblArtikel(admin.ModelAdmin):
    list_display = ("judul","pub_date","upload_berkas")

class TblAuthor(admin.ModelAdmin):
    list_display = ("nama_penulis", "email")

admin.site.register(Category)
admin.site.register(Autor, TblAuthor)
admin.site.register(Artikel, TblArtikel)