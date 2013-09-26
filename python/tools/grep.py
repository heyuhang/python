# -*- coding:utf-8 -*-
import os
import time 
from threading import Thread

def cdcGrep(cdcpath, keyword):
    filelist=os.listdir(cdcpath)
    for cdc in filelist:
        if ".cdc" in cdc:
            cdcfile=open(cdcpath+cdc)
            for line in cdcfile.readlines():
                if keyword in line:
                    print line
def cdcGrepl(cdcfile, keyword):
    cdcfd = open(cdcfile)
    report = ""
    for line in cdcfd.readlines():
        if keyword in line:
            report+=line
            report+=" "
    return report

class grepIt(Thread):
    def __init__(self, cdcfile, keyword):
        Thread.__init__(self)
        self.cdcf = cdcfile
        self.keyw = keyword.upper()
        self.report = ""
    def run(self):
        if ".cdc" in self.cdcf:
            self.report = cdcGrepl(self.cdcf, self.keyw)

def grpSearch(cdcpath, keyword):
    begin = time.time()
    filelist = os.listdir(cdcpath)
    searchlist = []
    for cdcf in filelist:
        pathcdcf = "%s/%s" % (cdcpath, cdcf)
        current = grepIt(pathcdcf, keyword)
        searchlist.append(current)
        current.start()
    for searcher in searchlist:
        searcher.join()
        print "Search from ",searcher.cdcf," out\n ",searcher.report
    print "usage %s s" % (time.time()-begin)
if __name__== '__main__':
    grpSearch("/home/heyuhang/python/cdc","h")
