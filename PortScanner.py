import sys
import socket


ip = f"{sys.argv[1]}"                                               #enter the IP address
open_ports=[]                                                       #the array that will be populated with ports

ports = range(1,65535)                                              #ports to be scanned

def probe_port(ip, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Create a socket object
        sock.settimeout(0.5)                                        # Set a timeout for the socket connection
        r = sock.connect_ex((ip, port))                             # Attempt to connect to the specified IP and port
        if r==0:                                                    # If the connection is successful (r == 0), update the result
            result = r

        sock.close()                                                #close the socket

    except Exception as e:                                          # If an exception occurs (e.g., socket error), ignore it
        pass
    return result                                                   # 0 when open, 1 when closed


for port in ports:
    sys.stdout.flush()                                              # Flush the standard output buffer
    response = probe_port(ip,port)                                  #call the function to check the port on the given ip

    if response == 0:                                               #if open, add to the array
        open_ports.append(port)

if open_ports:
    print("open ports are: ")
    print (sorted(open_ports))

else:
    print ("no open ports")

