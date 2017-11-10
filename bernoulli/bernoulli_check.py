#!/usr/bin/env python

def distance(a, b):
    return sum([(x-y)**2 for x,y in zip(a,b)])

f = [[float(y) for y in x.split(',')] for x in open("pis_new").read().split(";")]
g = [[float(y) for y in x.split(',')] for x in open("pis").read().split(";")]

h = [float(x) for x in open("qs_new").read().split(";")]
i = [float(x) for x in open("qs").read().split(";")]

print sum([distance(x, y) for x,y in zip(f, g)]) + len(f[0]) * sum([(x-y)**2 for x,y in zip(h,i)])

