#!/usr/bin/env python


networkfile='/home/haoyuw/twitter/v3/sub_v3.txt'
newfile='network.txt'

user_list = []
follower = {}
for line in open(networkfile):
    linelist = line.strip().split()
    user = int(linelist[0])
    user_list += [user]
    if len(linelist) < 2:
        continue
                                        
    follower[user] = [int(item) for item in linelist[1].split(',')]

user_set = set(user_list)
follower_dict = {}
for user, followers in follower.items():
    follower_dict[user] = list(set(followers) & user_set)

fout = open(newfile, 'w')
for user, followers in sorted(follower_dict.items(), key=lambda item:item[0]):
    followline = ",".join( [str(item) for item in followers] )
    fout.write("%s\t%s\n" % (user, followline))
fout.close()
