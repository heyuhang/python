import random

print "random 1-9 int: %d"%random.randint(1,9)

print "random 20-200 even: %d"%random.randrange(20, 201, 2)

print "random 0-1 float: %f"%random.random()
print "random 1-20 float: %f"%random.uniform(1, 20)

import string

print "random (a-z):%c"%random.choice('abcdefghijklmnopqrstuvwxyz')
print "string (spring,summer,fall,winter)%s"%random.choice(['spring','summer','fall','winter'])
print "random string:%s"%string.join(random.sample('abcdefghijklmnopqrstuvwxyz',4))


items = [1,2,3,4,5,6,7,8,9,0]
print '%s'%items
random.shuffle(items)
print 'result of sort:\n%s'%items
