![darth-vader](https://github.com/MuhiEddinTahhan/vader/assets/96084107/7b0e2894-b6e1-4d24-85eb-98da3a95cb9f)

# vader
an open-source cybersecurity tools written in python
# Upcoming updates:
1- add more tools.
2- add a command line interface and a command line banner

# HashCracker.py
a program that uses python library "hashlib" to crack md5 hash code by using a word list that is given by the user to the program. the program, will encode each line of the given list and will try to compare the hash until there is a match
# Upcoming updates:
1- more hash libraries will be added

# PortScanner.py
program that scan ports using python library "socket". the program will try to search for open ports given the IP address by the user. the program will create a socket object, set a timeout for the socket connection, and attempt to connect to the specified IP and port. if the connection fails, it will be given the code 1. if the connection successed, it will be given the code 0 and the program will append the port number in the array that lists the open ports to show it to the user.

# SSHBruteForce.py
program that uses "paramiko" library to preform ssh connection. after given the IP target, username, and path to the password list by the user, the program will establish a connection and open afile that will be used to enumerate through the list. It will stop at the first success entry and will record the password
# Upcoming updates:
1- use threads to make the enumeration faster.

# direnum.py
a program that uses "request" library to enumerate through directories of a given dns, or IP target. after giving a wordlist to the program and IP or dns of the target, it will start enumerating the wordlist to find directories in the target. 
# Upcoming updates:
1- add more status codes for the if statement
2- add php to the enumeration

# subdomainenum.py
uses the same mechanisim and libraries as the direnum.py to find the subdomain of a target.
# Upcoming updates:
1- add more protocols like https
