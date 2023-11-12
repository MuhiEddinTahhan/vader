import requests
import sys

""" define the subdomain list and put it in directory variable """

sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

"""construct a for loop that enumerates through the given list within the given IP or DNS to get results"""
for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"       #get the IP or DNS from command line
    r = requests.get(dir_enum)                          #GET requests evaluation
    if r.status_code == 404:                            #if code is 404 "not found"
        pass
    else:
        print("valid directory: ", dir_enum)            #print valid directory


"""
to improve:
1- there are other codes to be added like 500's, 300's etc
2- add php enumeration as well

"""