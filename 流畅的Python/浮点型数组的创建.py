from array import array
from random import random
import os
from time import perf_counter as pc

t1 = pc()
floats = array('d',(random() for i in range(10**7)))
print(floats[-1])

fp = open("floats.bin","wb")
floats.tofile(fp)
fp.close()
print(os.path.getsize("floats.bin")/2**10,'KB')

floats2 = array("d")
fp = open("floats.bin","rb")
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1])
print(floats==floats2 )
print(pc()-t1)
