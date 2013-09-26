
year=raw_input("input a year:");
year=int(year)
if year%400==0:
    print "%d is rui year\n" % year
elif year%4==0 and year%100!=0:
    print "%d is rui year\n" % year
else: print "%d is not rui year\n" % year
