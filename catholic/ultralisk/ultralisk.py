enc = open("flag.enc", "rb").read().encode('hex')
dec = ''

for i in range(0, len(enc), 4):
	dec += chr(int(enc[i], 16) * int(enc[i + 1] + enc[i + 2], 16) + int(enc[i + 3], 16))

open("flag.png", "wb").write(dec)
