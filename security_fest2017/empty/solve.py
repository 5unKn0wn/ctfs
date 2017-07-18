with open("./empty.pdf", "rb") as f:
	pdf = f.read()

table = pdf.split('/Widths[/Widths[')[1].split(']')[0].split(' ')
print ''.join(chr(int(i)) for i in table)
