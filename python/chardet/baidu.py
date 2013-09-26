import urllib

rawdata = urllib.urlopen("http://www.baidu.com").read()

import chardet

chardet.detect(rawdata)
