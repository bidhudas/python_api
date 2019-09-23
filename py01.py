#!/usr/bin/python3

svrlist = ["pcscf", 'scscf', 'tcscf']

print(svrlist[0])

svrlist2 = ["cscf", ["scscf", "icscf", "pcscf"], "tas", "hss"]

print(svrlist2[1][1])

#
svrlist.append("qcscf")

print(svrlist)

svrlist = svrlist + ["5g"]

print(svrlist)
