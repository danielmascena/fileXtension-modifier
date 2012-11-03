import os,glob,sys

try:
	current = sys.argv[1]
	new = sys.argv[2]
	os.chdir(sys.argv[3] if len(sys.argv) == 4 else os.curdir)
	for fi in glob.glob("*." + current):
   		os.rename(fi, fi[:-3] + new)
except IndexError:
	print "Type the correct files extensions [two expected]."     