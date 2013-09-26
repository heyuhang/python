import os.path

for path in ['/one/two/three', '/one/two/three', '/', '.', '']:
	print '"%s" : "%s"'%(path, os.path.split(path))

a = os.path.split("/home/heyuhang/heyu.c")
print "%s : %s"%(a[0],a[1])
