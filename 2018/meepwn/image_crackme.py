import subprocess
import os
import os.path
import time

inp = "MeePwn{"
ans = open("MeePwn.ascii.bak", "rt").read()
for a in range(32):
	ok = ' '
	for i in range(32, 127):
		p = subprocess.Popen('./image_crackme.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		p.stdin.write( inp + chr(i) + "\n" )
		p.stdout.readline()
		while True:
			if os.path.exists("MeePwn.ascii"):
				if open("MeePwn.ascii", "rt").read()[:len(inp) + 1] == ans[:len(inp) + 1]:
					ok = chr(i)
					print chr(i),
				os.system("del MeePwn.ascii")
				break
	inp += ok
	print
	print "cur inp : " + inp
