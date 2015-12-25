#! /usr/bin/python

# PNG2PDF - Image to pdf converting function.

from wand.image import Image
from wand.exceptions import BlobError

# Create a PDF named fileName from fileList image files
def imgConvert(fileList=[], fileName=''):
    """
    Convert images from fileList in pdf file named fileName.
    """
    with Image() as img:
        for file in fileList:
            try:
                img.read(filename=file)
            except BlobError as e:
                x = e.args[0]
                raise IOError(x)
            with img.convert('pdf') as converted:
                try:
                    converted.save(filename=fileName)
                except BlobError as e:
                    x = e.args[0]
                    raise IOError(x)
                except IOError as e:
                    x = e.args[0]
                    raise IOError(x)
