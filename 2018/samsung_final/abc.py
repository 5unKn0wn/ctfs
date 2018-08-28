# SCTF{H0w_b34u7ifu1_7h3_4u7om47ic_p47ch3r_i5!}
from pwn import *
from os import system

r = remote("abc.eatpwnnosleep.com", 55555)

for i in range(100):
        print "[*] TRY %d/100" % (i + 1)
	r.recvuntil("[*] TRY %d/100\n" % (i + 1))
	dat = r.recvuntil("[*]", drop=True).rstrip()
	r.recvuntil("You can only modify the binary with ")
	m_num = int(r.recvuntil(" byte(s)", drop=True))
	open("bin", "wb").write(dat.decode('base64'))
	system("objdump -M intel -d ./bin > objd.txt")
	objd = open("objd.txt", "rt").read()
	pt1 = int(objd.split("<read@plt>")[1].split("\n")[-4].split(":")[0].lstrip(), 16) + 2
	pt2 = int(objd.split("mov    rax,QWORD PTR [rax+0x10]")[1].split(":\t48 8d 3d ")[-2].split("\n")[-1].lstrip(' '), 16) + 3
	pt2_val = int(objd.split("mov    rax,QWORD PTR [rax+0x10]")[1].split(":\t48 8d 3d ")[-1][:2], 16) + 6
	pt3 = int(objd.split("mov    rax,QWORD PTR [rax+0x10]")[2].split("48 89 c7")[0].split(":")[0].split("    ")[1], 16) + 2
	pt4 = int(objd.split("jge")[0].split("\n")[-1].split(":")[0].lstrip(' '), 16)
	print hex(pt1), hex(pt2), hex(pt2_val), hex(pt3), hex(pt4)
	r.sendlineafter("[?] INPUT 1: ", "%s, 0x00" % hex(pt1))
	r.sendlineafter("[?] INPUT 2: ", "%s, %s" % (hex(pt2), hex(pt2_val)))
	r.sendlineafter("[?] INPUT 3: ", "%s, 0xc6" % hex(pt3))
	r.sendlineafter("[?] INPUT 4: ", "%s, 0x90" % hex(pt4))
	r.sendlineafter("[?] INPUT 5: ", "%s, 0x90" % hex(pt4+1))
        system("rm bin objd.txt")

r.interactive()
