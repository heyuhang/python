# -*- coding:utf-8 -*-
from ConfigParser import *
def iniCDinfo(cdrom,cdcfile):
    walker = {}
    for root, dirs, files in os.walk(cdrom):
        walker[root]=(dirs, files)
        cfg = RawConfigParser()
        cfg.add_section("Info")
        cfg.add_section("Comment")
        cfg.set("Info", 'ImagePath', cdrom)
        cfg.set("Info", 'Volumn', cdcfile)
        dirs = walker.keys()
        i=0
        for d in dirs:
            i+=1;
            cfg.set("Comment", str(i),d)
        for p in walker:
            cfg.add_section(p)
            for f in walker[p][1]:
                cfg.set(p, f, os.stat("%s/%s" % (p, f)).st_size)
        cfg.write(open(cdcfile, "w"))
