#usage
#python sff.to.trimmed.fastq.py <input.file.ssf> <output.file.fastq>
#		0			1		2

import sys
from Bio import SeqIO

#input
filein=open(sys.argv[1],"r")

#outputs
myout=sys.argv[2]
fileout=open(myout,'w')


SeqIO.convert(filein,"sff",fileout,"fastq")
