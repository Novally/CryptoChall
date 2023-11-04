from pwn import *

# Paste nc: 
host = ""
port = 

s = remote(host, port)

print(s.recv())

s.close()
