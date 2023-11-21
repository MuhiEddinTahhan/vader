import sys
import requests

"""define the list of enumeration"""

def subdomainenum_fun():
    sub_list = str(input('input the wordlist location: '))      #insert the location of the wordlist
    ip_address=str(input('insert IP address here: '))           #insert IP address
    wordlist = open(sub_list).read()                            #read the wordlist
    sub = wordlist.splitlines()                                 #split the values

    #create a for loop that will enumerate through the list to find the subdomains needed

    for words in sub:
        subdomains= f"http://{words}.{ip_address}"      #get the IP from the command line and try the list

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