import time

print 'gmtime   :',time.gmtime()
print 'localtime:',time.localtime()
print 'mktime   :',time.mktime(time.localtime())

print
t = time.localtime()
print 'Day of month:',t.tm_mday
print 'Day of week:',t.tm_wday
print 'Day of year:',t.tm_yday

now = time.ctime()
print now
parsed = time.strptime(now)
print parsed
print time.strftime("%a %b %d %H:%M:%S:%Y",parsed)

import os

def show_zone_info():
	print '\tTZ    :',os.environ.get('TZ','(not set)') 
	print '\ttzname:',time.tzname
	print '\tZone  :,%d (%d)'%(time.timezone,(time.timezone/3600))
	print '\tDST   :',time.daylight
	print '\tTime  :',time.ctime()
	print

print 'Default :'
show_zone_info()

for zone in ['US/Eastern','US/Pacific','GMT']:
	os.environ['TZ'] = zone
	time.tzset()
	print zone,':'
	show_zone_info()
