#!/usr/bin/env python

from sklearn import linear_model
from sklearn import cross_validation
from sklearn.metrics import classification_report

import sys
import numpy as np
import os.path as path

import Loader

#trainfile='/home/yipei/Twitter/FeatureExtraction/data/trainfile/LRbase/110445334.txt'

def GetRank(coef):
    ranklist = []
    i = 0
    for item in coef:
        ranklist += [(i, item)]
        i += 1
    return sorted(ranklist, key=lambda item:item[1], reverse=True)


trainlist=sys.argv[1]
paramfile = 'param.log'
pfile = 'param_rank.csv'
pfile2 = 'param_val.csv'
cleanfile = 'param_merge.log'

pos_threshold = 10
effective = 0
f = open(paramfile, 'w')
f2 = open(cleanfile, 'w')
fp = open(pfile, 'w')
fp2 = open(pfile2, 'w')
for line in open(trainlist):
    trainfile = line.strip()
    X_list, Y_list, X_test_list, Y_test_list = Loader.LoadData(trainfile, 0.1, pos_threshold)

    if len(Y_list)==0:
        continue
    effective += 1
    print trainfile
    f.write(trainfile+'\n')
    f2.write(trainfile+'\n')

    logreg = linear_model.LogisticRegression()
    first = True
    for i in range(0, len(Y_list)):
        X=X_list[i]
        Y=Y_list[i]
        X_test = X_test_list[i]
        Y_test = Y_test_list[i]

        logreg.fit(X, Y)
        if first:
            coef = logreg.coef_
            first = False
        else:
            coef += logreg.coef_

        f.write("%s\n" % (",".join([str(item) for item in logreg.coef_])))
    #print "parameter, ", logreg.coef_
    #accuracy = cross_validation.cross_val_score(logreg, X_test, np.array(Y_test), cv=10)
    #print np.mean(accuracy)

        Y_predict = logreg.predict(X_test)
        target_list = ['not_retweet', 'retweet']
        print(classification_report(Y_test, Y_predict, target_names=target_list))
    paramline = ",".join( [ str(item) for item in coef/len(Y_list)] )
    f.write("%s\n" % (paramline))
    f2.write("%s\n" % (paramline))
    fp2.write("%s\n" % (paramline))

    ranklist = GetRank(coef[0])
    f2.write("%s\n" % (",".join([str(item[0]) for item in ranklist])))
    fp.write("%s\n" % (",".join([str(item[0]) for item in ranklist])))

f.close()
f2.close()
fp.close()
fp2.close()
print "effective ", effective
