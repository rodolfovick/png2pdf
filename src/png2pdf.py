#! /usr/bin/python

from convert import imgConvert

list = ['/tmp/ww.jpg', '/tmp/ww2.jpg']

try:
    imgConvert(list, '/tmp/ww.pdf')
except IOError as e:
    print('ERROR '+str(e.args))
