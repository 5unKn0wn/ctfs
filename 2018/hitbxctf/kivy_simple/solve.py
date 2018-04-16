import re

with open("disasm.txt", "rt") as f:
	data = f.read()

p = re.compile("LOAD_CONST.*.")
chars = p.findall(data)
chars.pop(-1)
chars = [eval(i.split('(')[1][:-1]) for i in chars]

flag = bytearray(chars.pop(0))
for i in range(0, len(chars), 2):
	flag[chars[i]] = chars[i + 1]

print flag
