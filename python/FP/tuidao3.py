for s in ["%s*%s=%s"%(x,x,x*y) for x in range(1,10) for y in range(1,10) if x<=y]:
	print s
