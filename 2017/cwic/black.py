table1 = [0x4F25A495, 0x4EFD329C, 0x4EF13DCE, 0x4F67B35A, 0x4E86C539, 0x4EBC79DF, 0x4F7524BF, 0x4F249ADE]
table2 = [0xE2E5D97D, 0x21A92048]

yeah = """code = ''
code += asm('mov rdx, %s', arch = 'amd64')
code += asm('pxor    xmm0, xmm0', arch = 'amd64')
code += asm('movd    xmm0, rdx', arch = 'amd64')
code += asm('CVTTSS2SI rdx, xmm0', arch = 'amd64')
code += asm('mov rax, %s', arch = 'amd64')
code += asm('xor rax, rdx', arch = 'amd64')
"""

fin = ''
for i in range(2):
	fin += yeah % (hex(table2[i]), hex(table1[i]))

print fin
