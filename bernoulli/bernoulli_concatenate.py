#!/usr/bin/env python

import sys

PI = []
Q = []

f = open("part-00000", "r").read().split("\n")[:-1]

for i in range(len(f) / 2):
    PI.append(f[2*i])
    Q.append(f[2*i+1])

g = open("pis", "w")
h = open("qs", "w")

g.write(";".join(PI))
h.write(";".join(Q))

g.close()
h.close()
