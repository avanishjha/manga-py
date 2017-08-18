#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lxml.html import document_fromstring
import re

domainUri = 'http://tenmanga.com'


def get_main_content(url, get=None, post=None):
    name = get_manga_name(url, get)
    return get('{}/book/{}.html'.format(domainUri, name))


def get_volumes(content=None, url=None):
    items = document_fromstring(content).cssselect('.chapter-name.long > a')
    return [i.get('href') + '1-150-1.html' for i in items]


def get_archive_name(volume, index: int = None):
    return 'vol_{:0>3}'.format(index)


def get_images(main_content=None, volume=None, get=None, post=None):
    items = document_fromstring(get(volume)).cssselect('.pic_box img.manga_pic')
    return [i.get('src') for i in items]

def __get_name(test):
    test = test.groups()[0]
    if test.rfind('.html') > 0:
        test = test[0:test.rfind('.html')]
    return test.replace('+', ' ')


def get_manga_name(url, get=None):
    _ = '\.com/book/([^/]+)'
    test = re.search(_, url)
    if test:
        return __get_name(test)
    test = re.search('\.com/chapter/.+', url)
    if test:
        test = document_fromstring(get(url)).cssselect('.read-page nav a[href*="/book/"]')
        if len(test):
            test = re.search(_, test[0].get('href'))
            return __get_name(test)
    return ''


if __name__ == '__main__':
    print('Don\'t run this, please!')
