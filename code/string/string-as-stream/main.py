#!/usr/bin/env python
# coding: utf-8

import StringIO


def _main():

    s = '''head
ああああああああああああああああああああああ
ああああああああああああああああああああああ
ああああああああああああああああああああああ
ああああああああああああああああああああああ
ああああああああああああああああああああああ
end'''

    stream = StringIO.StringIO(s)
    for line in stream:
        line = line.rstrip("\r\n")
        print(line)

_main()

