#! /usr/bin/env python

configfile= open("vlanconfig.cfg", "r")
configblog = configfile.read()
configlist = configblog.splitlines()
print(configlist)
configfile.close()
