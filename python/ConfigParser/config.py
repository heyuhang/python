from ConfigParser import ConfigParser
import os

filename = os.path.join('.','config.ini')
print filename

config = ConfigParser()
config.read(filename)

url = config.get('portal','url')
print url
