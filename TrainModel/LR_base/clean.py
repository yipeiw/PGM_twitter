#!/usr/bin/env python

import os.path as path
from collections import defaultdict

filepath='train.log'

def UpdatePerformance(performance, p, r, f, tag):
    performance[name, tag, 'p'] += float(p)
    performance[name, tag, 'r'] += float(r)
    performance[name, tag, 'f'] += float(f)
    return performance

def GetAve(performance, folds):
    result = {}
    for key, val in performance.items():
        (name, tag, t) = key
        result[tag, t] = val/float(folds)
    return result

record = {}

fin = open(filepath)
while True:
    numline = fin.readline()
    if numline.find('effective')!=-1:
        break
    pathline = fin.readline()
    name = path.basename(pathline)

    performance = defaultdict(float)
    for nfold in range(0, 5):
        head = fin.readline()
        null = fin.readline()
        notline = fin.readline()
        yesline = fin.readline()
        null = fin.readline()
        totalline = fin.readline()
        null = fin.readline()

        tag, p, r, f, s = notline.split()
        performance = UpdatePerformance(performance, p, r, f, tag)
        tag, p, r, f, s = yesline.split()
        performance = UpdatePerformance(performance, p, r, f, tag)
        tag,fake1,fake2, p, r, f, s = totalline.split()
        performance = UpdatePerformance(performance, p, r, f, tag)

    record[name] = GetAve(performance, 5)

fin.close()

ave = defaultdict(float)
for name, result in record.items():
    print name
    for key, val in result.items():
        print key, val
        ave[key] += val

for key, val in ave.items():
    print key, val/float(95)

