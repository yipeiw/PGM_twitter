#!/usr/bin/env python

from collections import defaultdict

def addrelation(source, followers, relation_dict):
    for follow in followers:
        relation_dict[(source, follow)] = True
    return relation_dict

def outputGraph(filepath, follower, constrain, source=-1):
    fout = open(filepath, 'w')
    if constrain==-1:
        for user, follower_list in follower.items():
            for other in follower_list:
                fout.write("%s,%s\n" % (user, other))
    else:
        source_list = [source]
        relation_dict = defaultdict(bool)
        all_list = [source]
        for step in range(0, constrain):
            new_source_list = []
            for s in source_list:
                relation_dict = addrelation(s, follower[s], relation_dict)
                new_source_list += follower[s]
    
            source_list = new_source_list
            all_list += source_list
            print "nodes %s %s" % (len(all_list), len(list(set(all_list))))
        print "source %s relation size %s" % (source, len(relation_dict.keys()))
        for user, follow in sorted(relation_dict.keys(), key=lambda item:item[0]):
            fout.write("%s,%s\n" % (user, follow))
    fout.close()
