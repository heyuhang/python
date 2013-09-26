def foo(perms, x):
	i = 0
	print (perms,x)
	while perms[i]**2 <= x:
		print "( %d %d)"%(perms[i], x)
		if x%perms[i] == 0:
			return perms
		else:
			i += 1
	else:
		perms.append(x)
	return perms

print reduce(foo, range(5, 100, 2), [2, 3])
