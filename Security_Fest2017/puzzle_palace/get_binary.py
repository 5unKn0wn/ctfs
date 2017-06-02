from pwn import *

r = remote("pwn.ctf.rocks", 6666)

binary = ""
r.sendlineafter("#>", str(1))
r.recvuntil("A message glows brightly on the wall of this room [")
binary += r.recv(128)
print "recved... 0",

try:
	for i in range(200):
		print str(i + 1),
		r.sendlineafter("#>", str(2))
		r.recvuntil("A message glows brightly on the wall of this room [")
		binary += r.recv(128)
except:
	with open("puzzle_palace", "wb") as f:
		print binary.encode('hex')
		f.write(binary.decode('hex'))
		log.info("binary saved")
