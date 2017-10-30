from pwn import *

table1 = [0x4F25A495, 0x4EFD329C, 0x4EF13DCE, 0x4F67B35A, 0x4E86C539, 0x4EBC79DF, 0x4F7524BF, 0x4F249ADE]
table2 = [0xE2E5D97D, 0x21A92048, 0xAFDD362, 0x84DA3FA6, 0x7304E65E, 0x6F549BDD, 0xC149E05D, 0xD9D9EF37]

yeah = """code += asm('mov rdx, %s', arch = 'amd64')
code += asm('pxor    xmm0, xmm0', arch = 'amd64')
code += asm('movd    xmm0, rdx', arch = 'amd64')
code += asm('cvttss2si rdx, xmm0', arch = 'amd64')
code += asm('mov rax, %s', arch = 'amd64')
code += asm('xor rax, rdx', arch = 'amd64')
"""

fin = 'code = ""\n'
for i in range(8):
	fin += yeah % (hex(table1[i]), hex(table2[i]))

exec(fin)

print code.encode('hex')

# FLAG{n0_s4crific3zf0rth1s_m4g1C}
