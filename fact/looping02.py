#!/usr/bin/env python3

dnsfile = open("dnsservers.txt","r")

dnalist = dnsfile.readlines();


for svr in dnalist:

    print(svr, end="");

dnsfile.close()



