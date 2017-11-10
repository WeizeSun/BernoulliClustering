#!/usr/bin/env python

import sys
import math
import operator

def bernoulli(x, q):
    temp = [b if a == 1 else 1 - b for a,b in zip(x,q)]
    return reduce(operator.mul, temp, 1)

def gamma(x, Q, PI):
    Z = [pi * bernoulli(x, q) for pi,q in zip(PI, Q)]
    return [float(i) / sum(Z) for i in Z]

PI = [float(x) for x in sys.argv[1].split(";")]
Q = [[float(y) for y in x.split(",")] for x in sys.argv[2].split(";")]
#PI = [float(x) for x in open("pis", "r").read().split(";")]
#Q = [[float(y) for y in x.split(",")] for x in open("qs", "r").read().split(";")]
#f = open("bernoulli_train", "r")

for line in sys.stdin:
    item = line.split()
    label = int(item[0])
    features = [int(x) for x in item[1:]]
    gamma_xn = gamma(features, Q, PI)
    for i in range(len(PI)):
        print "{0}\t0\t{1}".format(i, ",".join([str(gamma_xn[i]*x) for x in features]))
        print "{0}\t1\t{1}".format(i, gamma_xn[i])

