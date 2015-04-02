# encoding: utf-8
'''
Copyright (c) 2013 Safari Books Online. All rights reserved.
'''

import uuid

from django.test import TestCase

from storage import models

class TestModels(TestCase):
    def setUp(self):
        self.book = models.Book.objects.create(title="The Title", pk=str(uuid.uuid4()))
        self.book_alias = models.Alias.objects.create(book=self.book, value=str(uuid.uuid4()), scheme=str(uuid.uuid4()))

    def test_book_have_unicode_method(self):
        '''The Book should have a __unicode__ method.'''
        expected = 'Book {}'.format(self.book.title)
        self.assertEquals(expected, unicode(self.book))

    def test_book_have_unicode_method(self):
        '''The Book should have a __unicode__ method.'''
        expected = '{} identifier for {}'.format(self.book_alias.scheme, self.book.title)
        self.assertEquals(expected, unicode(self.book_alias))


