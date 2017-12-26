from pwn import *
import json

r = remote("sss.eatpwnnosleep.com", 18878)

a = {
    'apikey' :'1064c753291615a28d8d443a9762f06cf24ff96dd0bb21601f75a8032743f233',
}

r.send(json.dumps(a).encode())
r.sendlineafter("finish", "valenv.c")
with open("valenv.c", "rt") as f:
	data = f.read().encode('base64').replace('\n', '')

r.sendlineafter("base64 : ", data)

r.sendlineafter("finish", "asttree.c")
with open("asttree.c", "rt") as f:
	data = f.read().encode('base64').replace('\n', '')
r.sendlineafter("base64 : ", data)

r.interactive()
