#!/usr/bin/env python

import sys
import random

f = [[float(y) / 255 for y in x.split(',')] for x in open("centroids", "r").read().split(";")]
g = open("qs", "w")
f = ';'.join([str(z) for z in [','.join([str(y) for y in x]) for x in f]])
g.write(f)
g.close()
print 'Now qs is ready'
f = [float(x.split()[4]) / 10000 for x in open("accuracy", "r").read().split("\n")[:-2]]
g = open("pis", "w")
g.write(";".join([str(x) for x in f]))
g.close()
print 'Now pis is ready'
