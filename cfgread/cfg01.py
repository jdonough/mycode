#! /usr/bin/env python

configfile = open("vlanconfig.cfg", "r")
print(configfile.read())
configfile.close 

configfile = open("vlanconfig.cfg", "r")
configlist = configfile.readlines()
print(configlist)
for x in configlist:
    print(x, end="")

configfile.close


