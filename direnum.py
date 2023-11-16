import requests
import sys

""" define the subdomain list and put it in directory variable """

def direnum_fun():
    sub_list = str(input('input the wordlist location: '))      #insert the location of the wordlist
    ip_address=str(input('insert IP address here: '))           #insert IP address
    wordlist = open(sub_list).read()                            #read the wordlist
    directories = wordlist.splitlines()                         #split the values

#construct a for loop that enumerates through the given list within the given IP or DNS to get results
    try:
        for dir in directories:
            dir_enum = f"http://{ip_address}/{dir}.html"       #get the IP or DNS from command line
            r = requests.get(dir_enum)                          #GET requests evaluation
            if r.status_code == 404:                            #if code is 404 "not found"
                pass
            else:
                print("valid directory: ", dir_enum)            #print valid directory
    except TimeoutError:                                        # throw an exception if time out
        print("please check if the IP address is correct")


"""
to improve:
1- there are other codes to be added like 500's, 300's etc
2- add php enumeration as well

"""