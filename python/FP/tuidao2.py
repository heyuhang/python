def isSymmetry(it):
	if it < 10:
		return True
	s = str(it)
	mpoint = len(s)-1;
	if(s[0] == s[mpoint]):
		return True
	else:
		return False

print [x for x in range(1000) if isSymmetry(x)]

