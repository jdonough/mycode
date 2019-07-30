#! /usr/bin/env python3

import shutil
import os
# set home directory
os.chdir('/home/student/mycode/')
# move raynor.obj to ceph_storage directory
shutil.move('raynor.obj', 'ceph_storage/')
# ask user for filename
xname = input(' What is the new name for kerrigan.obj? ')
# change kerrigan.obj to input name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

