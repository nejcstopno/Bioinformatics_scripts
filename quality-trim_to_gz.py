# Does not check for quality encoding but for a B as indicator of bad quality.
# use it with caution 

#!/usr/bin/env python

import sys
import screed
import gzip

# python quality-trim.py <input fastq file> <output filtered fastq file>
# MINLENGTH is the minimum lenth of read desired.  NCALLS is the percentage of a read with 'N' base calls for which if read has greater, it will be removed. 

MINLENGTH = 30

filein = sys.argv[1]
fileout = sys.argv[2]

fw = gzip.open(fileout, 'w')

count=0
for n, record in enumerate(screed.open(filein)):
    name = record['name']
    sequence = record['sequence']
    accuracy = record['accuracy']

    sequence = sequence.rstrip('N')
    accuracy = accuracy[:len(sequence)]

    if 'N' in sequence:
       continue
    else:
        trim = accuracy.find('B')

        if trim > MINLENGTH or (trim == -1 and len(sequence) > MINLENGTH):
            if trim == -1:
                fw.write('@%s\n%s\n+\n%s\n' % (name, sequence, accuracy))
            else:
                fw.write('@%s\n%s\n+\n%s\n' % (name, sequence[:trim], accuracy[:trim]))
            count += 1

    if n % 1000 == 0:
        print 'scanning', n

print 'Original Number of Reads', n + 1
print 'Final Number of Reads', count
print 'Total Filtered', n + 1  - int(count)
