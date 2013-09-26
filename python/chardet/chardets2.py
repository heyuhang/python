import urllib
import glob

from chardet.universaldetector import UniversalDetector

usock = urllib.urlopen('http://www.baidu.com')

detector = UniversalDetector()

for filename in glob.glob('*.py'):
	print filename.ljust(60),
	detector.reset()
	for line in file(filename, 'rb'):
		detector.feed(line)
		if detector.done:break
	detector.close()
	print detector.result
