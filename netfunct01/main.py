#!/usr/bin/env python3

import crayons

def commandpush(devicemd):


    for ip in devicemd.keys():
        
        for mycmds in devicemd[ip]:

            print(f'Attempting to sending command --> {crayons.red(mycmds)}')
        
    return None

def devicereboot(iplist):

    for x in iplist:
        print(f'Connecting to.. {crayons.white(x)}')
    print("Rebooting NOW!")


def main():

    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    
    commandpush(devicecmd)
    devicereboot(devicecmd);


main()


