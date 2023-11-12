import sys
import requests

"""define the list of enumeration"""
sub_list = open("wordlist.txt").read()
sub_enum = sub_list.splitlines()

"""create a for loop that will enumerate through the list to find the subdomains needed"""

for sub in sub_enum:
    subdomains= f"http://{sub}.{sys.argv[1]}"      #get the IP from the command line and try the list

    try:
        requests.get(subdomains)                        #GET protocol for the subdomain

    except requests.ConnectionError:                    #if there is a connection error or the subdomain doesn't work, pass
        pass

else:
    print ("valid subdomain: ", subdomains)             #print the valid subdomains

"""
to improve:
1- try other protocols like https
"""