# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify

class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __unicode__(self):
        return self.title

class Food(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True, verbose_name=u"Photo")
    description = models.TextField(max_length=200)
    category = models.ForeignKey('Category', verbose_name='Catégorie',
                                 help_text=u'Choisissez une catégorie pour ce contenu')
    meal = models.ManyToManyField(Meal, blank=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = u'Catégories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
