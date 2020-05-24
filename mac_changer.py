#!/usr/bin/env python

import subprocess
import os


def main():
    devnull = open(os.devnull, 'w')
    #  Remove : so it is 12 digits like mac  see how to count integers only
    currentmac = subprocess.call("ifconfig eth0 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'", shell=True,
                                 stdout=devnull, stderr=devnull)
    mac = input("Please enter a 12 digit MAC: ")

    if len(mac) == 12:

        if mac != currentmac:
            subprocess.call("ifconfig eth0 down", shell=True)
            subprocess.call(f'ifconfig eth0 hw ether {mac}', shell=True)
            subprocess.call("ifconfig eth0 up", shell=True)
            print(f'Mac Address has been changed to {mac}')

        else:
            print("Failed to change MAC Address. Please choose a different MAC.")
            return main()

    else:
        print("Invalid input or MAC. TIP: There must be an input of 12 digits, Example = 1122334455")
        return main()


main()
