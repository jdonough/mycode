#! /usr/bin/env python3
# setup input question
hostname = input("What value should we set for hostname? ")
# setup if statement make case insensative by making entry lowercase
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
# exit sctript statement to know it is complete
else:
    print("WRONG ANSWER")

print("Exiting the script")
