# encoding: utf-8

from django.db import models


class BaseModel(models.Model):
    '''Base class for all models'''
    created_time = models.DateTimeField('date created', auto_now_add=True)
    last_modified_time = models.DateTimeField('last-modified', auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    '''
    Main storage for a Book object.
    '''

    id = models.CharField(max_length=30, primary_key=True, help_text="The primary identifier of this title, we get this value from publishers.")
    title = models.CharField(max_length=128, help_text="The title of this book.", db_index=True, null=False, blank=False)
    description = models.TextField(blank=True, null=True, default=None, help_text="Very short description of this book.")

    def __unicode__(self):
        return u"Book %s" % self.title

    class Meta:
        ordering = ['title']


class Alias(BaseModel):
    '''
    A book can have one or more aliases which

    For example, a book can be referred to with an ISBN-10 (older, deprecated scheme), ISBN-13 (newer scheme),
    or any number of other aliases.
    '''

    book = models.ForeignKey(Book, related_name='aliases')
    value = models.CharField(max_length=255, db_index=True, help_text="The value of this identifier")
    scheme = models.CharField(max_length=40, help_text="The scheme of identifier")

    def __unicode__(self):
        return '%s identifier for %s' % (self.scheme, self.book.title)

    class Meta:
        unique_together = ('book', 'value', 'scheme')