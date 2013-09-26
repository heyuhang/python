try:
	import cPickle as pickle
except:
	import pickle
import pprint

data = [{'a':'A','b':2,'c':3.0}]
print 'DATA:'
pprint.pprint(data)

data_string = pickle.dumps(data)
print 'PICKLE:',data_string
#数据被序列化后就可以写入文件，socket，管道
