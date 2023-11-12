import hashlib

wordlist_location = str(input('input the wordlist location: '))                     #ask for directory to wordlist
hash_input = str(input('input a hash to be cracked: '))                             #ask for the hash

with open(wordlist_location, 'r', encoding='latin-1', errors='replace') as file:    #read the wordlist
    for line in file.readlines():                                                   #for each line
        try:    
            hash_object = hashlib.md5(line.strip().encode())                        #turn the first line to a hash
            hash_pass = hash_object.hexdigest()                                     # turn it to hex
        
            if hash_pass == hash_input:                                             #if value matches the hash input then show it
                print ('found cleartext passwor: '+ line.strip())
                exit(0)
        except UnicodeDecodeError:                                                  #if line can't be encoded throw exception
            print('Error decoding this line: ', line.strip())

print ('value not found')
            
"""
to improve:
1- include more hashes and already built in library
2- try to keep the program on until the user exits
"""