# encoding: utf-8

from django.db import models


class BaseModel(models.Model):
    '''Base class for all models'''
    created_time = models.DateTimeField('date created', auto_now_add=True)
    last_modified_time = models.DateTimeField('last-modified', auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    identifier = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=128, help_text="The title of the entry", db_index=True, null=False, blank=False)
    description = models.TextField(blank=True, null=True, default=None, help_text="Very short description, for list pages")

    def __unicode__(self):
        return u"Book %s" % self.title

    class Meta:
        ordering = ['title']


class Identifier(BaseModel):
    book = models.ForeignKey(Book, related_name='identifiers')
    identifier = models.CharField(max_length=255, db_index=True, unique=True)
    scheme = models.CharField(max_length=40)

    def __unicode__(self):
        return '%s identifier for %s' % (self.scheme, self.book.title)
