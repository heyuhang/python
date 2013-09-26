#!/usr/bin/python
# -*- coding:utf-8 -*-

""" HTML to text
@author: heyuhang
@version: 0.1
"""
import os
from html2text import *
import chardet
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

BAIDU_DIR = '/home/heyuhang/python/cdc/'
BAIDU_TXT = BAIDU_DIR+'baidu.txt'

def html_to_txt():
    ft = open(BAIDU_TXT,'w')
    start = 1
    while 1:
        filename = BAIDU_DIR+str(start)+'.html'
        if os.path.isfile(filename):
            fp = open(filename, 'r')
            htmltxt = ''.join(fp.readlines())
            if not htmltxt or not len(htmltxt):
                continue
            fp.close()

            codedetect = chardet.detect(htmltxt)["encoding"]
            print codedetext
            if not codedetect in ['utf-8', 'ascii']:
                htmltxt = unicode(htmltxt, codedetect).encode('utf-8')
                codedetect = chardet.detect(htmltxt)["encoding"]
                print 'change', codedetect

            ft.write(html2txt(htmltxt))
            print 'Success change html to txt %s' % start
            start+=1
        else:
            break
    ft.close()

if __name__ == '__main__':
    html_to_txt()

