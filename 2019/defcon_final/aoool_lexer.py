# It finds first 2 lexer
lex_arr = [0x1cL, 0x29L, 0x34L, 0x3L, 0x13L, 0x16L, 0x23L, 0x18L, 0x19L, 0x1aL, 0xaL, 0x32L, 0xcL, 0xdL, 0xeL, 0x2cL, 0x2dL, 0x2eL, 0xeL, 0xfL, 0x10L, 0x3cL, 0x5L, 0xcL, 0xdL, 0xeL, 0x4cL, 0x13L, 0x18L, 0x7L, 0x8L, 0xeL, 0xeL, 0x15L, 0x0L, 0x4bL, 0x4L, 0x9L, 0x16L, 0xfL, 0x5L, 0x16L, 0x16L, 0x16L, 0xfL, 0xfL, 0x4aL, 0x6L, 0x16L, 0x16L, 0xaL, 0x1aL, 0xfL, 0x16L, 0xbL, 0x16L, 0x14L, 0x9L, 0x14L, 0x14L, 0x45L, 0x13L, 0x0L, 0x0L]
off_arr = [-0xfL, 0x8L, 0x11L, 0x12L, 0xcL, 0x22L, 0xcdL, 0xcdL, 0xbL, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0x20L, 0x1cL, 0x10L, 0x13L, 0x14L, 0x4L, 0xcdL, 0xcdL, 0x18L, 0x23L, 0x1dL, 0x20L, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0x4L, 0xefL, 0x15L, 0x1eL, 0x29L, 0x1aL, 0x23L, 0xcdL, 0xcdL, 0x4L, 0x4L, 0x4L, 0xcdL, 0x1bL, 0x16L, 0x28L, 0xcdL, 0x29L, 0x19L, 0x19L, 0xcdL, 0xcdL, 0x1fL, 0x21L, 0x24L, 0x28L, 0xcdL, 0x2bL, 0xcdL, 0xcdL, 0xcdL, 0xcdL, 0x25L, 0x26L, 0x2bL, 0xcdL, 0x2aL, 0xcdL, 0xcdL, 0x20L, 0x23L, 0x29L, 0x27L, 0xcdL, 0xffL, 0xcdL]
lex_dict = {
	0x03 : "main", 
	0x04 : "root", 
	0x05 : "log", 
	0x06 : "mode", 
	0x07 : "text", 
	0x08 : "osl", 
	0x09 : "server_name", 
	0x0a : "server", 
	0x0b : "location", 
	0x0c : "print", 
	0x0d : "del", 
	0x0e : "`undefined symbol`", 
	0x0f : "`some string`", 
	0x10 : "`some number`", 
	0x11 : "(", 
	0x12 : ")", 
	0x13 : "{", 
	0x14 : "}", 
	0x15 : "=", 
	0x16 : ";", 
	0x17 : ",", 
	0x18 : "-", 
	0x19 : "+", 
	0x1a : "*"
}
start_sym = []

for i in range(3, 0x1b):
	if lex_arr[i] == i:
		start_sym.append(i)

for i in range(len(start_sym)):
	for j in range(3, 0x1b):
		if lex_arr[off_arr[i] + j] == j:
			print lex_dict[start_sym[i]], lex_dict[j]