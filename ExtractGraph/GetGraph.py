#!/usr/bin/env python

"""
1.Get the graph of 1000 nodes;
2.propogate 2-4 length to construct some smaller graph
format: if connected <node>,<node>
"""

import os.path as path
from collections import defaultdict

import Writer

networkfile = 'network.txt'
outputPath='graphs'

def GenerateSubgraph(name, outputPath):
    s2file = path.join(outputPath, str(name)+'_s2.csv')
    s3file = path.join(outputPath, str(name)+'_s3.csv')
    s4file = path.join(outputPath, str(name)+'_s4.csv')

    Writer.outputGraph(s2file, follower, 2, name)
    Writer.outputGraph(s3file, follower, 3, name)
    Writer.outputGraph(s4file, follower, 4, name)

follower = defaultdict(list)
rank_list = []
for line in open(networkfile):
    linelist = line.strip().split()
    user = int(linelist[0])
    if len(linelist) < 2:
        continue

    follower[user] = [int(item) for item in linelist[1].split(',')]
    rank_list.append( (user, len(follower[user])) )

rank_list = sorted(rank_list, key=lambda item:item[1], reverse=True)

allfile = path.join(outputPath, 'all_1000.csv')
Writer.outputGraph(allfile, follower, -1)

select = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
for rank in select:
    print rank_list[rank]
    GenerateSubgraph(rank_list[rank][0], outputPath)

