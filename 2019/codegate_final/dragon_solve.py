from pwn import *

r = remote("110.10.147.117", 12257)

r.recvuntil("=================================================================================================================\n")
dat = r.recvuntil("=================================================================================================================", drop=True).decode('base64')
open("dragon_elf", "wb").write(dat)

alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
table = bytearray(dat[0x8134:0x8134+52])
print table
r.sendlineafter("2> No I'm not\n", "1")
r.sendlineafter("2> No. I will waiting for them.\n", "1")
r.sendlineafter("2> I will chase him!\n", "2")

idxs = [table.index(i) for i in xor(dat[0x329c:0x329c+4], "\x55\x48\x89\xE5")]
key1 = bytearray("\x00" * 4)
for i in range(len(idxs)):
	idx = idxs[i]
	if idx + 0x47 <= 96:
		key1[i] = idx + 0x41
	elif idx + 0x41 > 96:
		key1[i] = idx + 0x47
	else:
		c1 = idx + 0x41
		c2 = idx + 0x47
		if chr(c1) in alphanum and chr(c2) not in alphanum:
			key1[i] = c1
		elif chr(c2) in alphanum and chr(c1) not in alphanum:
			key1[i] = c2
		else:
			print "Fuck, retry"
			exit(0)
print key1
r.sendlineafter("enter the key.\n", key1)

# ================ stage1 ======================
r.sendlineafter("2> I am a greatest king, so I can go there! Let's go down this cliff.", "1")	# 0 0 0 0 1
r.sendlineafter("2> Yes. I want.", "2")
r.sendlineafter("2> Check if it can make a flame.", "1")
r.sendlineafter("2> Take the sword and fight against it.", "2")
r.sendlineafter("2> I will check the dragon.", "2")
r.sendlineafter("2> Not fix it.", "1")
r.sendlineafter("2> The dragon will be surprise, so I will go to the servant.", "2")	# 0 2 1 1 1

idxs = [table.index(i) for i in xor(dat[0x2612:0x2612+10], "\x55\x48\x89\xE5\x48\x83\xEC\x20\x48\x89")]
key2 = bytearray("\x00" * 10)
for i in range(len(idxs)):
	idx = idxs[i]
	if idx + 0x47 <= 96:
		key2[i] = idx + 0x41
	elif idx + 0x41 > 96:
		key2[i] = idx + 0x47
	else:
		c1 = idx + 0x41
		c2 = idx + 0x47
		if chr(c1) in alphanum and chr(c2) not in alphanum:
			key2[i] = c1
		elif chr(c2) in alphanum and chr(c1) not in alphanum:
			key2[i] = c2
		else:
			print "Fuck, retry"
			exit(0)
print key2
r.sendlineafter("enter the key.\n", key2)

# ================ stage2 ======================
r.sendlineafter("2> Find the food for the dragon.", "2")
r.sendlineafter("2> Not give the food.", "1")
r.sendlineafter("2> Go to the palace.", "1")
r.sendlineafter("2> Go to the palace.", "1")
r.sendlineafter("2> Go to the palace.", "2")
r.sendlineafter("2> Don't ask.", "2")
r.sendlineafter("3> Don't want to know about the dragon.", "2")

idxs = [table.index(i) for i in xor(dat[0x1d9c:0x1d9c+10], "\x55\x48\x89\xE5\x48\x83\xEC\x20\x48\x89")]
key3 = bytearray("\x00" * 10)
for i in range(len(idxs)):
	idx = idxs[i]
	if idx + 0x47 <= 96:
		key3[i] = idx + 0x41
	elif idx + 0x41 > 96:
		key3[i] = idx + 0x47
	else:
		c1 = idx + 0x41
		c2 = idx + 0x47
		if chr(c1) in alphanum and chr(c2) not in alphanum:
			key3[i] = c1
		elif chr(c2) in alphanum and chr(c1) not in alphanum:
			key3[i] = c2
		else:
			print "Fuck, retry"
			exit(0)
print key3
r.sendlineafter("enter the key.\n", key3)

# ================ stage3 ======================
r.sendlineafter("2> Conquer neighboring country.", "1")
r.sendlineafter("2> For 7 days.", "2")
r.sendlineafter("4> North", "1")
r.sendlineafter("4> North", "1")
r.sendlineafter("4> North", "1")
r.sendlineafter("4> North", "1")

idxs = [table.index(i) for i in xor(dat[0x164d:0x164d+10], "\x55\x48\x89\xE5\x48\x83\xEC\x20\x48\x89")]
key4 = bytearray("\x00" * 10)
for i in range(len(idxs)):
	idx = idxs[i]
	if idx + 0x47 <= 96:
		key4[i] = idx + 0x41
	elif idx + 0x41 > 96:
		key4[i] = idx + 0x47
	else:
		c1 = idx + 0x41
		c2 = idx + 0x47
		if chr(c1) in alphanum and chr(c2) not in alphanum:
			key4[i] = c1
		elif chr(c2) in alphanum and chr(c1) not in alphanum:
			key4[i] = c2
		else:
			print "Fuck, retry"
			exit(0)
print key4
r.sendlineafter("enter the key.\n", key4)

# ================ stage4 ======================
r.sendlineafter("2> Let's go to see the ocean on the cliff.", "1")
r.sendlineafter("2> Scold a dragon.", "2")
r.sendlineafter("2> Follow him.", "2")
r.sendlineafter("2> No, I won't.", "1")

idxs = [table.index(i) for i in xor(dat[0x102e:0x102e+10], "\x55\x48\x89\xE5\x48\x83\xEC\x20\x48\x89")]
key5 = bytearray("\x00" * 10)
for i in range(len(idxs)):
	idx = idxs[i]
	if idx + 0x47 <= 96:
		key5[i] = idx + 0x41
	elif idx + 0x41 > 96:
		key5[i] = idx + 0x47
	else:
		c1 = idx + 0x41
		c2 = idx + 0x47
		if chr(c1) in alphanum and chr(c2) not in alphanum:
			key5[i] = c1
		elif chr(c2) in alphanum and chr(c1) not in alphanum:
			key5[i] = c2
		else:
			print "Fuck, retry"
			exit(0)
print key5
r.sendlineafter("enter the key.\n", key5)

# ================ stage5 ======================
r.sendlineafter("2> I will give the dragon to other country", "1")
for i in range(3):
	r.sendlineafter("East : ", "99")
	r.sendlineafter("West : ", "99")
	r.sendlineafter("South : ", "99")
	r.sendlineafter("North : ", "99")

r.interactive()


