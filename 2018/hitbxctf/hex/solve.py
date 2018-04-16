import re

with open("disasm.txt", "rt") as f:
	data = f.read()

p = re.compile(".*.ldi     r22, .*")
chars = p.findall(data)
chars = [int(i.split(", ")[1].split(" ;")[0], 16) for i in chars]
string = ""

for c in chars:
	if c > 0x7f:
		continue
	string += chr(c)

print string
