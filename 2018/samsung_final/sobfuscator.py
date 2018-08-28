# gdb -q smachine -x sobfuscator.py
import gdb
import os

script = """
set $base=0x0000555555554000
set $inp=0x55555c75b560

def fn
	del
	b *($base + 0x3b6a)
	r prob.bin <<< $arg1
	del
	watch *(int *)($inp+$arg0*4)
	c
	c
	c
	c
	c
	c
	end

fn %d %s
"""

flag = [1] * 32
for i in range(32):
        open("gdbscript", "w").write(script % (i, ''.join(chr(i) for i in flag)))
        gdb.execute("source gdbscript")
        res = gdb.execute("p $rax", to_string=True)
        flag[i] = (flag[i] - int((res.split(' = ')[1]), 16)) & 0xff
        print(''.join(chr(i) for i in flag))

print("flag : " + ''.join(chr(i) for i in flag))
os.system("rm gdbscript peda-session-smachine.txt")
