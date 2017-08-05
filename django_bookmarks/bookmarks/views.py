# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    ouput = '''
        <html>
            <head>
                <title>%s</title>
            </head>
            <body>
                <h1>%s</h1><p>%s</p>
            </body>
        </html>
    ''' % ( 
            '장고 | 북마크',
            '장고 북마크 웰컴!',
            '북마크 저장해 줘요~'
    )

    return HttpResponse(ouput)
