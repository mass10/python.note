#!/usr/bin/env python
# coding: utf-8
#
# old-fashined http request styles.
#

import urllib
#import urllib2

def _do_get():

    response = urllib.urlopen('https://www.google.com').read()
    print response

def _do_post():

    params = {'q': 'jenkins ci', 'key-1': 'value 1', 'key-2': 'value 2'}
    params = urllib.urlencode(params)
    stream = urllib.urlopen('https://www.google.com/search', params)
    print stream.read()

def _main():

    # _do_get()
    _do_post()

_main()

