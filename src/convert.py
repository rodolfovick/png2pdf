#! /usr/bin/python

from wand.image import Image

def imgConvert(fileList=[], fileName=''):
    with Image() as img:
        for file in fileList:
            img.read(filename=file)
            with img.convert('pdf') as converted:
                converted.save(filename=fileName)
