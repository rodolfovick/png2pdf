#!/usr/bin/env python

from distutils.core import setup

setup(name='PNG2PDF',
      version='0.1',
      description='Image to PDF converter',
      author='Rodolfo Vick',
      author_email='rodolfo.vick@gmail.com',
      url='https://github.com/rodolfovick/png2pdf/',
      py_modules=['png2pdf'],
      data_files=[('/usr/share/applications/', ['misc/png2pdf.desktop']),
                  ('/usr/share/pixmaps/', ['misc/png2pdf.png']),
                  ('/usr/bin/', ['misc/png2pdf'])]
     )
