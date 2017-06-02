# ls -tr ./qrcodemadness | xargs | python solve.py
from qrtools import QR

l = raw_input().split(' ')

b = ''
for i in l:
	myCode = QR(filename="./qrcodemadness/" + i)
	myCode.decode()
	b += myCode.data
print b[58:].decode('base64').rstrip()
