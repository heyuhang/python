from commands import *
from shutil import *

print 'BEFORE:',getstatus('file_to_change.txt')
copymode('mode.py','file_to_change.txt')
print 'AFTER:',getstatus('file_to_change.txt')
