import os

from shutil import *

os.mkdir('example')

print 'BEFORE:',os.listdir('example')
copy('copys.py','example')
print 'ALFTER:', os.listdir('example')
