#! /usr/bin/env python3
import shutil
import os
# set home directory
os.chdir("/home/student/mycode/")
# copy sdn_network.txt to sdn_network.txt.copy
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
# creates 5g_research_backup folder and copies contents
shutil.copytree("5g_research/", "5g_research_backup/")
