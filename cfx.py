import os,glob,sys

os.chdir(os.curdir)
try:
	current = sys.argv[1]
	new = sys.argv[2]
	for fi in glob.glob("*." + current):
   		os.rename(fi, fi[:-3] + new)
except IndexError:
	print "Type the correct files extensions [two expected]."     