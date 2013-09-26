import hashlib
import time

# Used to calculate the MD5 checksum data

data = open(__file__,'rt').read()

for i in range(5):
	h = hashlib.sha1()
	print time.ctime(), ': %0.3f %0.3f'%(time.time(),time.clock())
	for i in range(100000):
		h.update(data)
	cksum = h.digest()
