#! /usr/bin/python

from wand.image import Image
from wand.exceptions import BlobError

# Create a PDF named fileName from fileList image files
def imgConvert(fileList=[], fileName=''):
    with Image() as img:
        for file in fileList:
            try:
                img.read(filename=file)
            except BlobError:
                raise IOError
            with img.convert('pdf') as converted:
                try:
                    converted.save(filename=fileName)
                except BlobError:
                    raise IOError
                except IOError:
                    raise IOError
