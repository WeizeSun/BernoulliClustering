#!/usr/bin/env python

import sys
import operator

cur_centroid = None
cur_num = 0
cur_sum_features = None

count = 0
total_images = 0
total_correct = 0

for line in sys.stdin:
    key, value = line.split()
    key = int(key)
    value = int(value)
    if cur_centroid is None:
        cur_centroid = key
        cur_num = 1
        cur_dict = {value: 1}
    elif cur_centroid != key:
        print "Cluster Number: {0}\t#images: {1}\tMajor Label: {2}\t#correctly clustered images: {3}\tAccuracy%: {4}".format(count, cur_num, max(cur_dict.iteritems(), key=operator.itemgetter(1))[0], max(cur_dict.iteritems(), key=operator.itemgetter(1))[1], max(cur_dict.iteritems(), key=operator.itemgetter(1))[1] / float(cur_num))
        total_images += cur_num
        total_correct += max(cur_dict.iteritems(), key=operator.itemgetter(1))[1]
        count += 1
        cur_num = 1
        cur_dict = {value: 1}
        cur_centroid = key
    elif cur_centroid == key:
        cur_num += 1
        cur_dict[value] = cur_dict.get(value, 0) + 1

print "Cluster Number: {0}\t#images: {1}\tMajor Label: {2}\t#correctly clustered images: {3}\tAccuracy%: {4}".format(count, cur_num, max(cur_dict.iteritems(), key=operator.itemgetter(1))[0], max(cur_dict.iteritems(), key=operator.itemgetter(1))[1], max(cur_dict.iteritems(), key=operator.itemgetter(1))[1] / float(cur_num))
total_images += cur_num
total_correct += max(cur_dict.iteritems(), key=operator.itemgetter(1))[1]

print "Total #images: {0}\tTotal #correctly clustered images: {1}\tAccuracy: {2}".format(total_images, total_correct, float(total_correct) / total_images)

