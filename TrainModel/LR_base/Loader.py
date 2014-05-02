#!/usr/bin/env python
import random

def LoadData(trainfile, test_percent, small, folds=5):
    feat_pool = []
    lb_pool = []

    num = 0
    pos_num = 0
    for line in open(trainfile):
        linelist = line.strip().split(',')
        lb = int(linelist[0])
        if lb > 0:
            pos_num += 1

        lb_pool += [lb]
        feat_pool.append([int(item) for item in linelist[1:len(linelist)]])
        num += 1
    if pos_num<small:
        return [],[],[],[]

    print pos_num, num
    threshold = float(pos_num)/(num-pos_num)
    
    train_feat_list=[]
    train_lb_list = []
    test_feat_list = []
    test_lb_list = []

    for i in range(0, folds):
        train_feat, train_lb, test_feat, test_lb = Sample(feat_pool, lb_pool, test_percent, threshold)
        train_feat_list.append(train_feat)
        train_lb_list.append(train_lb)
        test_feat_list.append(test_feat)
        test_lb_list.append(test_lb)
    return train_feat_list,train_lb_list,test_feat_list,test_lb_list

def Sample(feat_pool, lb_pool, percent, threshold):
    train_feat = []
    train_lb = []
    test_feat = []
    test_lb = []

    for n in range(0, len(lb_pool)):
        lb = lb_pool[n]
        feat = feat_pool[n]
        if random.uniform(0, 1) < percent:
            test_lb.append(lb)
            test_feat.append(feat)
            continue

        if lb<1:
            if random.uniform(0, 1) > threshold:
                continue
        
        train_lb.append(lb)
        train_feat.append(feat)

    return train_feat, train_lb, test_feat, test_lb 









