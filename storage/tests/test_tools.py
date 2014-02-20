# encoding: utf-8
# Created by David Rideout <drideout@safaribooksonline.com> on 2/7/14 5:01 PM
# Copyright (c) 2013 Safari Books Online, LLC. All rights reserved.

from django.test import TestCase
from lxml import etree
from storage.models import Book, Identifier
import storage.tools


class TestTools(TestCase):
    def setUp(self):
        pass

    def test_storage_tools_process_book_element_db(self):
        '''process_book_element should put the book in the database.'''

        xml_str = '''
        <book id="12345">
            <title>A title</title>
            <aliases>
                <alias scheme="isbn10" identifier="0158757819"/>
                <alias scheme="proprietary" identifier="abcdefgh"/>
            </aliases>
        </book>
        '''

        xml = etree.fromstring(xml_str)
        storage.tools.process_book_element(xml)

        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.get(pk='12345')

        self.assertEqual(book.title, 'A title')
        self.assertEqual(book.identifiers.count(), 2)
        self.assertEqual(Identifier.objects.get(scheme='isbn10').identifier, '0158757819')
        self.assertEqual(Identifier.objects.get(scheme='proprietary').identifier, 'abcdefgh')

