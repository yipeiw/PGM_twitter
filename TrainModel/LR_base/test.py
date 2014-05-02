#!/usr/bin/env python

filepath='param_val.csv'
output='param_val_revised.csv'

fin = open(filepath)
fout = open(output, 'w')
for i in range(0, 96):
    l1=fin.readline().strip()
    l2=fin.readline().strip()
    l3=fin.readline().strip()
    outputline = ",".join(l1.split()+l2.split()+l3.split())
    fout.write(outputline + '\n')
fout.close()
fin.close()
