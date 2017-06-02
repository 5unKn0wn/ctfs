table = '''8D 9D 8A 98 A5 BB BF AC  B2 A7 81 BB BF AC B2 A7
81 AD AB B0 BA BF A7 81  B3 B1 AC B0 B7 B0 B9 E1
A3'''.replace(' ', '').replace('\n', '').decode('hex')

print ''.join(chr(ord(i) ^ 0xde) for i in table)
