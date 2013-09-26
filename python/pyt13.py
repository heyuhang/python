# -*- coding:utf-8 -*-
import sys, cmd
from pyt11 import *
from grep import *
class PyCDC(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.CDROM='/home/heyuhang/'
        self.CDDIR='cdc/'
        self.prompt="(PyCDC)>"
        self.intro='''CDC 使用说明:
    dir  目录名  #指定保存和搜索目录
    walk 文件名  #指定光盘信息文件名
    find 关键词  #使用在保存和搜索目录中遍历所有cmd文件 找含有关键字的那一行
    ？           #查询
    EOF          #推出系统
    '''
    def help_EOF(self):
        print "推出程序"
    def do_EOF(self, line):
        sys.exit()

    def help_walk(self):
        print "扫描管盘内容"
    def do_walk(self, filename):
        if filename=="":
            filename=raw_input("输入cmd文件名:")
        print "扫描光盘内容保存到: '%s'" % filename
        cdWalker(self.CDROM, self.CDDIR+filename)

    def help_dir(self):
        print "指定保存/搜索目录"
    def do_dir(self, pathname):
        if pathname=="":
            pathname=raw_input("请输入指定保存/搜索目录:")
        self.CDDIR=pathname
        print "指定保存/搜索目录：'%s',默认是: '%s'" % (pathname, self.CDDIR)

    def help_find(self):
        print "搜索关键词"
    def do_find(self, keyword):
        if keyword=="":
            keyword=raw_input("请输入搜索关键词:")
        print "搜索关键词: '%s'" %keyword
        grpSearch(self.CDROM, keyword)

if __name__ == '__main__':
    cdc=PyCDC()
    cdc.cmdloop()
