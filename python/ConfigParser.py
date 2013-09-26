# -*- coding:utf-8 -*-
from ConfigParser import RawConfigPaser as rcp

cfg = rcp()

cfg.add_section("Info")
cfg.set("Info", "ImagePath", "/home/heyuhang/cdc/heyu.cdc")
cfg.set("Info", "foo", "CD 信息")
cfg.write(open("try.ini", "w"))

