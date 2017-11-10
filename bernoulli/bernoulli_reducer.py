#!/usr/bin/env python

import sys

cur_k = None
cur_vec = None
cur_num = None
cur_sum = None

for line in sys.stdin:
    k, code, item = line.split()
    k = int(k)
    if code == '0':
        numerator = [float(x) for x in item.split(',')]
    else:
        denominator = float(item)

    if cur_k == None:
        cur_k = k
        cur_vec = numerator
        cur_num = 1
        cur_sum = 0
    elif cur_k != k:
        print "{0}".format(float(cur_sum) / cur_num)
        print "{0}".format(",".join([str(float(x) / cur_sum) for x in cur_vec]))
        cur_k = k
        cur_vec = [0] * len(cur_vec)
        cur_num = 1
        cur_sum = 0
    elif cur_k == k:
        if code == '0':
            cur_vec = [x+y for x,y in zip(cur_vec, numerator)]
            cur_num += 1
        elif code == '1':
            cur_sum += denominator

print "{0}".format(float(cur_sum) / cur_num)
print "{0}".format(",".join([str(float(x) / cur_sum) for x in cur_vec])) 
