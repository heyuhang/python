import os
import time
from shutil import *

def show_file_info(filename):
	stat_info = os.stat(filename)
	print '\tMode    :',stat_info.st_mode
	print '\tCreated :',time.ctime(stat_info.st_ctime)
	print '\tAccessed:',time.ctime(stat_info.st_atime)
	print '\tModified:',time.ctime(stat_info.st_mtime)

os.mkdir('example')
print 'SOURCE:'
show_file_info('copy3.py')
copy2('copy3.py','example')
print 'DEST:'
show_file_info('example/copy3.py')
