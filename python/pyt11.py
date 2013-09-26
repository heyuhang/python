# -*- coding: utf-8 -*-
import os
import chardet

def _smartcode(stream):
    """
    smart recove stream into UTF-8
    """
    ustring=stream
    codedetect=chardet.detect(ustring)["encoding"]
    print codedetect

    try:
        print ustring
        ustring=unicode(ustring, codedetect)
        print ustring
        return "%s %s" % ("",ustring.encode('utf-8'))
    except:
        return u"bad unicode encode try!"
def formatCDinfo(root, dirs, files):
    export="\n"+root+"\n"
    for d in dirs:
        export+="-d"+root+_smartcode(d)+"\n"
    for f in files:
        export+="-f %s %s \n" % (root, _smartcode(f))
    export+="="*70
    return export

def cdWalker(cdrom, cdcfile):
    export=""
    for root, dirs, files in os.walk(cdrom):
        export+=formatCDinfo(root, dirs, files)
    open(cdcfile, 'w').write(export)


if __name__ == '__main__':
    CDROM = '/home/heyuhang/'
    cdWalker(CDROM,"./cdctools.cdc")
