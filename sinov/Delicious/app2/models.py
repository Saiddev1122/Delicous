from django.db import models

# Create your models here.
from django.utils.text import slugify

from app2 import defaut_prep, rating


class Category(models.Model):
    name = models.CharField(max_length=400)
    slug = models.SlugField(unique=True, max_length=400, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    product = models.CharField(max_length=500)
    portsiya = models.CharField(max_length=256)

    def __str__(self):
        return self.product


class Recipes(models.Model):
    name = models.CharField(max_length=500)
    prep = models.JSONField(default=defaut_prep())
    image = models.ImageField(upload_to='static/site/img', blank=True)
    steps = models.TextField()
    Tayyorlash_uslubi_1 = models.TextField(blank=True)
    Tayyorlash_uslubi_2 = models.TextField(blank=True)
    Tayyorlash_uslubi_3 = models.TextField(blank=True)
    Tayyorlash_uslubi_4 = models.TextField(blank=True)
    Tayyorlash_uslubi_5 = models.TextField(blank=True)
    Tayyorlash_uslubi_6 = models.TextField(blank=True)
    Tayyorlash_uslubi_7 = models.TextField(blank=True)
    Tayyorlash_uslubi_8 = models.TextField(blank=True)
    Tayyorlash_uslubi_9 = models.TextField(blank=True)
    Tayyorlash_uslubi_10 = models.TextField(blank=True)
    Tayyorlash_uslubi_11 = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.SmallIntegerField(choices=rating())
    ingredient = models.ManyToManyField(Ingredients)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Admin(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    is_activate = models.BooleanField(default=True)
    is_both = models.BooleanField(default=False)

    def __str__(self):
        return self.username

