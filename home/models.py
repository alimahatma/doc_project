from pyexpat import model
from django.db import models

class Category (models.Model):

    name_category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name_category


class Autor (models.Model):

    nama_penulis = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.nama_penulis

class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    pub_date = models.DateField()
    kategori = models.ManyToManyField(Category)
    penulis = models.ManyToManyField(Autor)
    upload_berkas = models.FileField()

    def __str__(self):
        return (self.judul)




