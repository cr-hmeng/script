#!/usr/bin/python

import sys
import struct

if len(sys.argv) < 3:
    print 'usage:', sys.argv[0], '<file1>  <file2> '
    sys.exit(0)

#k  = int(sys.argv[3]) # parallel multiplers in a kernel (2)
#pc = int(sys.argv[4]) # parallel coefficients in a kernel (2)
##NF = int(sys.argv[2]) # number of filter
##NC = int(sys.argv[3]) # number of channels
##pf = int(sys.argv[4]) # number of channels

# read in the original file
b1_file = open(sys.argv[1], 'rb')
b1_data = b1_file.read()
b1_file.close()
print len(b1_data) 


c = []
for j in range (0, len(b1_data)/2):
    p = j*2
    c.append(struct.unpack('<H', b1_data[p:p+2])[0])

print len(c)

# output data for 1x1 requirements
b2_file = open(sys.argv[2], 'wb')
n = 0;

for j in range (0, len(b1_data)/2):
    b2_file.write(struct.pack('>H', c[j]))

b2_file.close()
