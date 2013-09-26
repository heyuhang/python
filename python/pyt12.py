# -*- coding: utf-8 -*-
import sys, cmd
from pyt09 import *

if __name__ == '__main__':
    cdc=PyCDC()
    cdc.cmdloop()
    CDROM='/home/heyuhang'
    cdWalker(CDROM, "cdctools.cdc")
