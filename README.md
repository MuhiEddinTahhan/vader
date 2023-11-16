![darth-vader](https://github.com/MuhiEddinTahhan/vader/assets/96084107/7b0e2894-b6e1-4d24-85eb-98da3a95cb9f)

# vader
an open-source cybersecurity tool written in Python.
## IMPORTANT NOTE:
users might need to install some python libraries to run the program like "requests"  
to install these libraries, on your terminal write:  
  pip3 install {wanted library}  
example:
  pip3 install requests
## Upcoming updates:
1- add more tools.  
2- add a command line interface and a command line banner.  

# HashCracker.py
A program that uses the Python library "hashlib" to crack md5 hash code by using a word list that is given by the user to the program. The program will encode each line of the given list and will try to compare the hash until there is a match.  
## Upcoming updates:
1- More hash libraries will be added.  

# PortScanner.py
A program that scans ports using the Python library "socket". the program will try to search for open ports given the IP address by the user. The program will create a socket object, set a timeout for the socket connection, and attempt to connect to the specified IP and port. If the connection fails, it will be given the code 1. If the connection succeeds, it will be given the code 0 and the program will append the port number in the array that lists the open ports to show it to the user.  

# SSHBruteForce.py
A program that uses the "paramiko" library to perform SSH connection. After giving the IP target, username, and path to the password list by the user, the program will establish a connection and open a file that will be used to enumerate through the list. It will stop at the first successful entry and will record the password.  
## Upcoming updates:
1- Use threads to make the enumeration faster.  

# direnum.py
A program that uses the "request" library to enumerate through directories of a given DNS, or IP target. After giving a wordlist to the program and the IP or DNS of the target, it will start enumerating the wordlist to find directories in the target. 
## Upcoming updates:
1- Add more status codes for the if statement.  
2- add PHP to the enumeration.  

# subdomainenum.py
The program uses the same mechanism and libraries as the direnum.py to find the subdomain of a target.  
## Upcoming updates:
1- Add more protocols like HTTPS.  
