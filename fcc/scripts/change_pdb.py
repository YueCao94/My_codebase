import numpy as np
import sys
import os

prot = sys.argv[1]

for filename in os.listdir(prot):
	with open("temp", "w") as fout:
		with open(prot+'/'+filename, "r") as fin:
			for line in fin:
				if(line[:2]=='AT'):
					fout.write(line[:-1]+"           "+line[12]+line[-1])
				else:
					fout.write(line)
	os.system("mv temp "+prot+'/'+filename)


