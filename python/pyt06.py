#-*- coding: utf-8 -*-
import os
filedir=os.listdir("/media/heyuhang/Ubuntu 12.1")
for files in filedir:
    fs = "/media/heyuhang/Ubuntu 12.1/"+files
    fd=file(fs,'r')
    for line in fd.readlines():
        print line
    fd.close()

    

