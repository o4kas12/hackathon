from pwn import *

r = remote("127.0.0.1", 80)

data = r.recv()
data = r.recv(1024)

r.send("123\n")

