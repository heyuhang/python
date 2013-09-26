try:
	import cPickle as pickle
except:
	import pickle
import pprint
from StringIO import StringIO
import sys

from pic3 import SimpleObject

try:
	filename = sys.argv[1]
except IndexError:
	raise RuntimeError('Please specify a filename as argument to %s'%sys.argv[0])

in_s = open(filename, 'rb')

try:
	while True:
		try:
			o = pickle.load(in_s)
		except EOFError:
			break
		else:
			print 'READ: %s (%s)'%(o.name, o.name_backwards)
finally:
	in_s.close()
