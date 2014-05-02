#!/usr/bin/env python

from collections import defaultdict
import os.path as path


retweetfile = '/home/haoyuw/twitter/v3/retweets.txt'

author_dict = defaultdict(lambda: defaultdict(int))
num_dict = defaultdict(int)

count = 0
for line in open(retweetfile):
    count += 1
    tweet_id, author, num, RT_list = line.strip().split()
    for RT in RT_list.split(','):
        author_dict[author][RT] += 1
    num_dict[author] += 1

outputPath = 'Info/retweet'
for author in author_dict.keys():
    outputfile = path.join(outputPath, author+'.txt')
    fout = open(outputfile, 'w')
    fout.write("total tweets: %s\n" % (num_dict[author]))
    for RT, number in sorted(author_dict[author].items(), key=lambda item:item[1], reverse=True):
        fout.write("%s:%s\n" % (RT, number))
        if float(number)/num_dict[author]> 0.5 and num_dict[author]>1:
            print "%s %s %s %s %s" % (author, len(author_dict[author].keys()), RT, num_dict[author], number)
    fout.close()
