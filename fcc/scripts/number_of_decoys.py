import sys
n=0
with open (sys.argv[1], "r") as f:
	for lines in f:
		line = lines.strip('\n').split()
		n+= len(line) -3

print ("number of decoys in the clusters:", n)

