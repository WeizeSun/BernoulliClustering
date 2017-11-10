#!/usr/bin/env python

import operator
import math

def bernoulli(x, q):
    temp = [max(b, 1e-10) if a == 1 else max(1 - b, 1e-10)  for a,b in zip(x, q)]
    return reduce(operator.mul, temp, 1)

def gamma(x, Q, PI):
    Z = [pi * bernoulli(x,q) for pi,q in zip(PI, Q)]
    return [float(i) / sum(Z) for i in Z]

f = open("bernoulli_train", "r")
g = open("bernoulli_results", "w")
h = open("bernoulli_for_accuracy", "w")

PI = [float(x) for x in open("pis", "r").read().split(";")]
Q = [[float(y) for y in x.split(",")] for x in open("qs", "r").read().split(";")]


count = 1
likelihood = 0
for line in f:
    item = line.split()
    label = int(item[0])
    features = [int(x) for x in item[1:]]
    gamma_xn = gamma(features, Q, PI)
    pi_gamma_xn = [pi*ga for pi,ga in zip(PI, gamma_xn)]
    cluster = max(enumerate(pi_gamma_xn), key=operator.itemgetter(1))[0]
    likelihood += math.log(sum(pi_gamma_xn))
    g.write("{0}\t{1}\n".format(count, cluster))
    count += 1
f.close()
g.close()
print likelihood

f = open("bernoulli_test", "r")
for line in f:
    item = line.split()
    label = int(item[0])
    features = [int(x) for x in item[1:]]
    gamma_xn = gamma(features, Q, PI)
    pi_gamma_xn = [pi*ga for pi,ga in zip(PI, gamma_xn)]
    cluster = max(enumerate(pi_gamma_xn), key=operator.itemgetter(1))[0]
    h.write("{0}\t{1}\n".format(cluster, label))
h.close()
f.close()
