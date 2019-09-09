global _start
section .text

_start:
	lea r9, &tbl1
	lea rsi, &tbl4
	mov ebx, [inp]
	mov eax, [inp + 4]
	lea r10, &tbl2
	mov r11d, [inp + 8]
	mov edx, [inp + 12]
	xor ebx, 0xa5f16b07
	xor eax, 0x35acc916
	mov ecx, ebx
	movzx edi, bl
	movzx ebp, bh
	shr ecx, 0x18
	mov r8d, eax
	xor r11d, 0xa82889f4
	mov ecx, dword [r9 + rcx*4]
	xor ecx, dword [rsi + rdi*4]
	mov edi, ebx
	shr edi, 0x10
	shr r8d, 0x18
	xor edx, 0xad0512c0
	movzx edi, dil
	mov r8d, dword [r10 + r8*4]
	xor ecx, dword [r10 + rdi*4]
	lea rdi, &tbl3
	xor ecx, dword [rdi + rbp*4]
	movzx ebp, al
	xor r8d, dword [r9 + rbp*4]
	mov ebp, eax
	shr ebp, 0x10
	movzx ebp, bpl
	xor r8d, dword [rdi + rbp*4]
	movzx ebp, ah
	xor r8d, dword [rsi + rbp*4]
	lea ebp, [rcx + r8]
	add ecx, 0x1887698A
	add ebp, 0x99371D48
	lea ecx, [rcx + r8*2]
	xor ebp, r11d
	movzx r8d, bpl
	xor edx, ecx
	mov ecx, ebp
	shr ecx, 0x18
	movzx r11d, dl
	mov ecx, dword [r9 + rcx*4]
	xor ecx, dword [rsi + r8*4]
	mov r8d, ebp
	shr r8d, 0x10
	movzx r8d, r8b
	xor ecx, dword [r10 + r8*4]
	mov r8d, edx
	shr r8d, 0x18
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + r11*4]
	mov r11d, edx
	shr r11d, 0x10
	mov r14d, ecx
	mov ecx, ebp
	movzx r11d, r11b
	movzx ecx, ch
	xor r8d, dword [rdi + r11*4]
	xor r14d, dword [rdi + rcx*4]
	movzx ecx, dh
	xor r8d, dword [rsi + rcx*4]
	mov ecx, 0x2FFE48CE
	add ecx, r14d
	lea r11d, [r14 + r8]
	add r11d, 0x4C4DF454
	lea ecx, [rcx + r8*2]
	xor eax, ecx
	xor r11d, ebx
	mov ecx, r11d
	movzx r8d, r11b
	mov ebx, r11d
	shr ecx, 0x18
	movzx ebx, bh
	ror ebp, 1
	mov ecx, dword [r9 + rcx*4]
	xor ecx, dword [rsi + r8*4]
	mov r8d, r11d
	shr r8d, 0x10
	movzx r8d, r8b
	xor ecx, dword [r10 + r8*4]
	mov r8d, eax
	xor ecx, dword [rdi + rbx*4]
	shr r8d, 0x18
	movzx ebx, al
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbx*4]
	mov ebx, eax
	shr ebx, 0x10
	movzx ebx, bl
	xor r8d, dword [rdi + rbx*4]
	movzx ebx, ah
	xor r8d, dword [rsi + rbx*4]
	lea ebx, [rcx + r8]
	add ecx, 0x7E1FD336
	add ebx, 0x9DC32A17
	lea r8d, [rcx + r8*2]
	xor ebp, ebx
	ror ebp, 2
	xor edx, r8d
	xor ebp, ebx
	mov ecx, edx
	ror ebp, 3
	rol ecx, 1
	xor ebx, ebp
	xor ecx, r8d
	mov ebp, ebx
	mov r12d, ebx
	rol ecx, 2
	ror ebp, 4
	xor ecx, r8d
	mov edx, ebp
	mov ebx, ebp
	rol ecx, 3
	shr edx, 0x18
	xor ecx, r8d
	mov edx, dword [r9 + rdx*4]
	rol ecx, 4
	xor ecx, r8d
	movzx r8d, bpl
	xor edx, dword [rsi + r8*4]
	mov r8d, ebp
	movzx ebp, bh
	shr r8d, 0x10
	movzx r8d, r8b
	xor edx, dword [r10 + r8*4]
	mov r8d, ecx
	xor edx, dword [rdi + rbp*4]
	movzx ebp, cl
	shr r8d, 0x18
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbp*4]
	mov ebp, ecx
	shr ebp, 0x10
	ror r11d, 1
	movzx ebp, bpl
	xor r8d, dword [rdi + rbp*4]
	movzx ebp, ch
	xor r8d, dword [rsi + rbp*4]
	mov ebp, 0x11B9FE7C
	add ebp, edx
	add edx, 0xCCBE2567
	add ebp, r8d
	xor r11d, ebp
	ror r11d, 2
	lea r8d, [rdx + r8*2]
	xor r11d, ebp
	ror r11d, 3
	xor eax, r8d
	xor ebp, r11d
	mov edx, eax
	mov r11d, ebp
	rol edx, 1
	ror r11d, 4
	xor edx, r8d
	mov eax, r11d
	mov ebx, r11d
	rol edx, 2
	shr eax, 0x18
	movzx ebx, bh
	xor edx, r8d
	mov eax, dword [r9 + rax*4]
	rol edx, 3
	xor edx, r8d
	rol edx, 4
	xor edx, r8d
	movzx r8d, r11b
	xor eax, dword [rsi + r8*4]
	mov r8d, r11d
	movzx r11d, dl
	shr r8d, 0x10
	movzx r8d, r8b
	xor eax, dword [r10 + r8*4]
	mov r8d, edx
	shr r8d, 0x18
	xor eax, dword [rdi + rbx*4]
	movzx ebx, dh
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + r11*4]
	mov r11d, edx
	shr r11d, 0x10
	movzx r11d, r11b
	xor r8d, dword [rdi + r11*4]
	mov r11d, 0x73CB587E
	xor r8d, dword [rsi + rbx*4]
	mov ebx, r12d
	ror ebx, 5
	add r11d, eax
	add eax, 0x0BB17DE52
	add r11d, r8d
	lea r8d, [rax + r8*2]
	mov eax, ecx
	mov ecx, ebx
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 2
	rol eax, 1
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 3
	rol eax, 2
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 4
	rol eax, 3
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 5
	rol eax, 4
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 6
	rol eax, 5
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 7
	rol eax, 6
	xor eax, r8d
	rol eax, 7
	xor r11d, ecx
	mov ebx, r11d
	xor eax, r8d
	ror ebx, 8
	rol eax, 8
	mov ecx, ebx
	xor eax, r8d
	movzx r8d, bl
	shr ecx, 0x18
	mov ecx, dword [r9 + rcx*4]
	xor ecx, dword [rsi + r8*4]
	mov r8d, ebx
	shr r8d, 0x10
	movzx ebx, bh
	movzx r8d, r8b
	xor ecx, dword [r10 + r8*4]
	mov r8d, eax
	xor ecx, dword [rdi + rbx*4]
	shr r8d, 0x18
	movzx ebx, al
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbx*4]
	mov ebx, eax
	shr ebx, 0x10
	movzx ebx, bl
	xor r8d, dword [rdi + rbx*4]
	movzx ebx, ah
	xor r8d, dword [rsi + rbx*4]
	mov ebx, 0x0E41A9E40
	add ebx, ecx
	add ecx, 0x20B6CA01
	add ebx, r8d
	lea r8d, [rcx + r8*2]
	xor edx, r8d
	mov ecx, edx
	mov edx, ebp
	ror edx, 5
	rol ecx, 1
	xor edx, ebx
	xor ecx, r8d
	ror edx, 2
	rol ecx, 2
	xor edx, ebx
	xor ecx, r8d
	ror edx, 3
	rol ecx, 3
	xor edx, ebx
	xor ecx, r8d
	ror edx, 4
	rol ecx, 4
	xor edx, ebx
	xor ecx, r8d
	ror edx, 5
	rol ecx, 5
	xor edx, ebx
	xor ecx, r8d
	ror edx, 6
	rol ecx, 6
	xor edx, ebx
	xor ecx, r8d
	ror edx, 7
	rol ecx, 7
	xor ebx, edx
	xor ecx, r8d
	mov ebp, ebx
	rol ecx, 8
	mov r12d, ebx
	ror ebp, 8
	xor ecx, r8d
	mov edx, ebp
	movzx r8d, bpl
	mov ebx, ebp
	shr edx, 0x18
	mov edx, dword [r9 + rdx*4]
	xor edx, dword [rsi + r8*4]
	mov r8d, ebp
	shr r8d, 0x10
	movzx ebp, bh
	movzx r8d, r8b
	xor edx, dword [r10 + r8*4]
	mov r8d, ecx
	xor edx, dword [rdi + rbp*4]
	shr r8d, 0x18
	movzx ebp, cl
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbp*4]
	mov ebp, ecx
	shr ebp, 0x10
	movzx ebp, bpl
	xor r8d, dword [rdi + rbp*4]
	movzx ebp, ch
	xor r8d, dword [rsi + rbp*4]
	mov ebp, 0x8A29375
	add ebp, edx
	add edx, 0xF45131B5
	add ebp, r8d
	lea r8d, [rdx + r8*2]
	xor eax, r8d
	mov edx, eax
	mov eax, r11d
	ror eax, 9
	rol edx, 1
	xor edx, r8d
	xor eax, ebp
	ror eax, 2
	rol edx, 2
	xor edx, r8d
	xor eax, ebp
	ror eax, 3
	rol edx, 3
	xor edx, r8d
	xor eax, ebp
	ror eax, 4
	rol edx, 4
	xor edx, r8d
	xor eax, ebp
	ror eax, 5
	rol edx, 5
	xor edx, r8d
	xor eax, ebp
	ror eax, 6
	rol edx, 6
	xor edx, r8d
	xor eax, ebp
	ror eax, 7
	rol edx, 7
	xor edx, r8d
	xor eax, ebp
	rol edx, 8
	ror eax, 8
	xor edx, r8d
	xor eax, ebp
	ror eax, 9
	rol edx, 9
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xa
	rol edx, 0xa
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xb
	rol edx, 0xb
	xor ebp, eax
	xor edx, r8d
	mov r11d, ebp
	rol edx, 0xc
	ror r11d, 0xc
	xor edx, r8d
	mov eax, r11d
	movzx r8d, r11b
	mov ebx, r11d
	shr eax, 0x18
	movzx ebx, bh
	mov eax, dword [r9 + rax*4]
	xor eax, dword [rsi + r8*4]
	mov r8d, r11d
	shr r8d, 0x10
	movzx r11d, dl
	movzx r8d, r8b
	xor eax, dword [r10 + r8*4]
	mov r8d, edx
	shr r8d, 0x18
	xor eax, dword [rdi + rbx*4]
	movzx ebx, dh
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + r11*4]
	mov r11d, edx
	shr r11d, 0x10
	movzx r11d, r11b
	xor r8d, dword [rdi + r11*4]
	mov r11d, 0x0EC86B94A
	xor r8d, dword [rsi + rbx*4]
	mov ebx, r12d
	ror ebx, 9
	add r11d, eax
	add eax, 0x0F434A484
	add r11d, r8d
	lea r8d, [rax + r8*2]
	mov eax, ecx
	mov ecx, ebx
	xor eax, r8d
	rol eax, 1
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 2
	rol eax, 2
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 3
	rol eax, 3
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 4
	rol eax, 4
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 5
	rol eax, 5
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 6
	rol eax, 6
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 7
	rol eax, 7
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 8
	rol eax, 8
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 9
	rol eax, 9
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 0xa
	rol eax, 0xa
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 0xb
	rol eax, 0xb
	xor r11d, ecx
	xor eax, r8d
	mov ebx, r11d
	rol eax, 0xc
	ror ebx, 0xc
	xor eax, r8d
	mov ecx, ebx
	movzx r8d, bl
	shr ecx, 0x18
	mov ecx, dword [r9 + rcx*4]
	xor ecx, dword [rsi + r8*4]
	mov r8d, ebx
	shr r8d, 0x10
	movzx ebx, bh
	movzx r8d, r8b
	xor ecx, dword [r10 + r8*4]
	mov r8d, eax
	xor ecx, dword [rdi + rbx*4]
	shr r8d, 0x18
	movzx ebx, al
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbx*4]
	mov ebx, eax
	shr ebx, 0x10
	movzx ebx, bl
	xor r8d, dword [rdi + rbx*4]
	movzx ebx, ah
	xor r8d, dword [rsi + rbx*4]
	mov ebx, 0xA297E6CA
	add ebx, ecx
	add ecx, 0xF77B1151
	add ebx, r8d
	lea r8d, [rcx + r8*2]
	xor edx, r8d
	mov ecx, edx
	mov edx, ebp
	ror edx, 0xd
	rol ecx, 1
	xor edx, ebx
	xor ecx, r8d
	ror edx, 2
	rol ecx, 2
	xor edx, ebx
	xor ecx, r8d
	ror edx, 3
	rol ecx, 3
	xor edx, ebx
	xor ecx, r8d
	ror edx, 4
	rol ecx, 4
	xor edx, ebx
	xor ecx, r8d
	ror edx, 5
	rol ecx, 5
	xor edx, ebx
	xor ecx, r8d
	ror edx, 6
	rol ecx, 6
	xor edx, ebx
	xor ecx, r8d
	ror edx, 7
	rol ecx, 7
	xor edx, ebx
	xor ecx, r8d
	ror edx, 8
	rol ecx, 8
	xor edx, ebx
	xor ecx, r8d
	ror edx, 9
	rol ecx, 9
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xa
	rol ecx, 0xa
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xb
	rol ecx, 0xb
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xc
	rol ecx, 0xc
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xd
	rol ecx, 0xd
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xe
	rol ecx, 0xe
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xf
	rol ecx, 0xf
	xor ebx, edx
	xor ecx, r8d
	mov ebp, ebx
	rol ecx, 0x10
	mov r12d, ebx
	rol ebp, 0x10
	xor ecx, r8d
	mov edx, ebp
	movzx r8d, bpl
	mov ebx, ebp
	shr edx, 0x18
	mov edx, dword [r9 + rdx*4]
	xor edx, dword [rsi + r8*4]
	mov r8d, ebp
	shr r8d, 0x10
	movzx ebp, bh
	movzx r8d, r8b
	xor edx, dword [r10 + r8*4]
	mov r8d, ecx
	xor edx, dword [rdi + rbp*4]
	shr r8d, 0x18
	movzx ebp, cl
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbp*4]
	mov ebp, ecx
	shr ebp, 0x10
	movzx ebp, bpl
	xor r8d, dword [rdi + rbp*4]
	movzx ebp, ch
	xor r8d, dword [rsi + rbp*4]
	mov ebp, 0x64031E7B
	add ebp, edx
	add edx, 0xB8441E91
	add ebp, r8d
	lea r8d, [rdx + r8*2]
	xor eax, r8d
	mov edx, eax
	mov eax, r11d
	ror eax, 0xd
	rol edx, 1
	xor eax, ebp
	xor edx, r8d
	ror eax, 2
	rol edx, 2
	xor eax, ebp
	xor edx, r8d
	ror eax, 3
	rol edx, 3
	xor eax, ebp
	xor edx, r8d
	ror eax, 4
	rol edx, 4
	xor eax, ebp
	xor edx, r8d
	ror eax, 5
	rol edx, 5
	xor eax, ebp
	xor edx, r8d
	ror eax, 6
	rol edx, 6
	xor eax, ebp
	xor edx, r8d
	ror eax, 7
	rol edx, 7
	xor eax, ebp
	xor edx, r8d
	ror eax, 8
	rol edx, 8
	xor eax, ebp
	xor edx, r8d
	ror eax, 9
	rol edx, 9
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xa
	rol edx, 0xa
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xb
	rol edx, 0xb
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xc
	rol edx, 0xc
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xd
	rol edx, 0xd
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xe
	rol edx, 0xe
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xf
	rol edx, 0xf
	xor ebp, eax
	xor edx, r8d
	mov r11d, ebp
	rol edx, 0x10
	rol r11d, 0x10
	xor edx, r8d
	mov eax, r11d
	movzx r8d, r11b
	mov ebx, r11d
	shr eax, 0x18
	movzx ebx, bh
	mov eax, dword [r9 + rax*4]
	xor eax, dword [rsi + r8*4]
	mov r8d, r11d
	shr r8d, 0x10
	movzx r11d, dl
	movzx r8d, r8b
	xor eax, dword [r10 + r8*4]
	mov r8d, edx
	shr r8d, 0x18
	xor eax, dword [rdi + rbx*4]
	movzx ebx, dh
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + r11*4]
	mov r11d, edx
	shr r11d, 0x10
	movzx r11d, r11b
	xor r8d, dword [rdi + r11*4]
	mov r11d, 0xF780D547
	xor r8d, dword [rsi + rbx*4]
	mov ebx, r12d
	rol ebx, 0xf
	add r11d, eax
	add eax, 0x73B43C69
	add r11d, r8d
	lea r8d, [rax + r8*2]
	mov eax, ecx
	mov ecx, ebx
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 2
	rol eax, 1
	xor ecx, r11d
	xor eax, r8d
	ror ecx, 3
	rol eax, 2
	xor eax, r8d
	rol eax, 3
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 4
	rol eax, 4
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 5
	rol eax, 5
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 6
	rol eax, 6
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 7
	rol eax, 7
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 8
	rol eax, 8
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 9
	rol eax, 9
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 0xa
	rol eax, 0xa
	xor eax, r8d
	xor ecx, r11d
	rol eax, 0xb
	ror ecx, 0xb
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 0xc
	rol eax, 0xc
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 0xd
	rol eax, 0xd
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 0xe
	rol eax, 0xe
	xor eax, r8d
	xor ecx, r11d
	ror ecx, 0xf
	rol eax, 0xf
	xor eax, r8d
	xor ecx, r11d
	rol ecx, 0x10
	rol eax, 0x10
	xor eax, r8d
	xor ecx, r11d
	rol ecx, 0xf
	ror eax, 0xf
	xor eax, r8d
	xor ecx, r11d
	rol ecx, 0xe
	ror eax, 0xe
	xor eax, r8d
	xor ecx, r11d
	rol ecx, 0xd
	ror eax, 0xd
	xor eax, r8d
	xor r11d, ecx
	mov ebx, r11d
	ror eax, 0xc
	rol ebx, 0xc
	xor eax, r8d
	mov ecx, ebx
	movzx r8d, bl
	shr ecx, 0x18
	mov ecx, dword [r9 + rcx*4]
	xor ecx, dword [rsi + r8*4]
	mov r8d, ebx
	shr r8d, 0x10
	movzx ebx, bh
	movzx r8d, r8b
	xor ecx, dword [r10 + r8*4]
	mov r8d, eax
	xor ecx, dword [rdi + rbx*4]
	shr r8d, 0x18
	movzx ebx, al
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbx*4]
	mov ebx, eax
	shr ebx, 0x10
	movzx ebx, bl
	xor r8d, dword [rdi + rbx*4]
	movzx ebx, ah
	xor r8d, dword [rsi + rbx*4]
	mov ebx, 0x65EA20DC
	add ebx, ecx
	add ecx, 0x2BE2BF0B
	add ebx, r8d
	lea r8d, [rcx + r8*2]
	xor edx, r8d
	mov ecx, edx
	mov edx, ebp
	rol edx, 0xf
	rol ecx, 1
	xor ecx, r8d
	xor edx, ebx
	ror edx, 2
	rol ecx, 2
	xor ecx, r8d
	xor edx, ebx
	ror edx, 3
	rol ecx, 3
	xor ecx, r8d
	xor edx, ebx
	ror edx, 4
	rol ecx, 4
	xor ecx, r8d
	xor edx, ebx
	ror edx, 5
	rol ecx, 5
	xor ecx, r8d
	xor edx, ebx
	ror edx, 6
	rol ecx, 6
	xor ecx, r8d
	xor edx, ebx
	ror edx, 7
	rol ecx, 7
	xor ecx, r8d
	xor edx, ebx
	ror edx, 8
	rol ecx, 8
	xor ecx, r8d
	xor edx, ebx
	ror edx, 9
	rol ecx, 9
	xor ecx, r8d
	xor edx, ebx
	ror edx, 0xa
	rol ecx, 0xa
	xor ecx, r8d
	xor edx, ebx
	ror edx, 0xb
	rol ecx, 0xb
	xor ecx, r8d
	xor edx, ebx
	ror edx, 0xc
	rol ecx, 0xc
	xor ecx, r8d
	xor edx, ebx
	ror edx, 0xd
	rol ecx, 0xd
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xe
	rol ecx, 0xe
	xor edx, ebx
	xor ecx, r8d
	ror edx, 0xf
	rol ecx, 0xf
	xor edx, ebx
	xor ecx, r8d
	rol edx, 0x10
	rol ecx, 0x10
	xor edx, ebx
	xor ecx, r8d
	rol edx, 0xf
	ror ecx, 0xf
	xor edx, ebx
	xor ecx, r8d
	rol edx, 0xe
	ror ecx, 0xe
	xor edx, ebx
	xor ecx, r8d
	rol edx, 0xd
	ror ecx, 0xd
	xor ebx, edx
	xor ecx, r8d
	mov edx, ebx
	ror ecx, 0xc
	mov r14d, ebx
	rol edx, 0xc
	xor ecx, r8d
	mov r8d, edx
	movzx ebp, dl
	shr r8d, 0x18
	mov r8d, dword [r9 + r8*4]
	xor r8d, dword [rsi + rbp*4]
	mov ebp, edx
	shr ebp, 0x10
	movzx edx, dh
	movzx ebp, bpl
	xor r8d, dword [r10 + rbp*4]
	movzx ebp, cl
	xor r8d, dword [rdi + rdx*4]
	mov edx, r8d
	mov r8d, ecx
	shr r8d, 0x18
	mov r8d, dword [r10 + r8*4]
	xor r8d, dword [r9 + rbp*4]
	mov ebp, ecx
	shr ebp, 0x10
	movzx ebp, bpl
	xor r8d, dword [rdi + rbp*4]
	movzx ebp, ch
	xor r8d, dword [rsi + rbp*4]
	mov ebp, 0x78EC4FCA
	add ebp, edx
	add edx, 0xDDFD9C3A
	add ebp, r8d
	lea r8d, [rdx + r8*2]
	xor eax, r8d
	mov edx, eax
	mov eax, r11d
	rol eax, 0xb
	rol edx, 1
	xor eax, ebp
	xor edx, r8d
	ror eax, 2
	rol edx, 2
	xor eax, ebp
	xor edx, r8d
	ror eax, 3
	rol edx, 3
	xor eax, ebp
	xor edx, r8d
	ror eax, 4
	rol edx, 4
	xor eax, ebp
	xor edx, r8d
	ror eax, 5
	rol edx, 5
	xor eax, ebp
	xor edx, r8d
	ror eax, 6
	rol edx, 6
	xor eax, ebp
	xor edx, r8d
	ror eax, 7
	rol edx, 7
	xor eax, ebp
	xor edx, r8d
	ror eax, 8
	rol edx, 8
	xor eax, ebp
	xor edx, r8d
	ror eax, 9
	rol edx, 9
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xa
	rol edx, 0xa
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xb
	rol edx, 0xb
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xc
	rol edx, 0xc
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xd
	rol edx, 0xd
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xe
	rol edx, 0xe
	xor eax, ebp
	xor edx, r8d
	ror eax, 0xf
	rol edx, 0xf
	xor eax, ebp
	xor edx, r8d
	rol eax, 0x10
	rol edx, 0x10
	xor eax, ebp
	xor edx, r8d
	rol eax, 0xf
	ror edx, 0xf
	xor eax, ebp
	xor edx, r8d
	rol eax, 0xe
	ror edx, 0xe
	xor eax, ebp
	xor edx, r8d
	rol eax, 0xd
	ror edx, 0xd
	xor eax, ebp
	xor edx, r8d
	rol eax, 0xc
	ror edx, 0xc
	xor eax, ebp
	xor edx, r8d
	rol eax, 0xb
	ror edx, 0xb
	xor eax, ebp
	xor edx, r8d
	rol eax, 0xa
	ror edx, 0xa
	xor eax, ebp
	xor edx, r8d
	rol eax, 9
	ror edx, 9
	xor ebp, eax
	xor edx, r8d
	mov r11d, ebp
	ror edx, 8
	rol r11d, 8
	xor edx, r8d
	mov eax, r11d
	movzx r8d, r11b
	mov ebx, r11d
	shr eax, 0x18
	movzx r12d, dl
	movzx ebx, bh
	mov eax, dword [r9 + rax*4]
	xor eax, dword [rsi + r8*4]
	mov r8d, r11d
	shr r8d, 0x10
	movzx r8d, r8b
	xor eax, dword [r10 + r8*4]
	mov r8d, edx
	shr r8d, 0x18
	xor eax, dword [rdi + rbx*4]
	movzx ebx, dh
	mov r11d, dword [r10 + r8*4]
	mov r8d, edx
	xor r11d, dword [r9 + r12*4]
	shr r8d, 0x10
	movzx r8d, r8b
	xor r11d, dword [rdi + r8*4]
	mov r8d, 0x7A462BD8
	xor r11d, dword [rsi + rbx*4]
	mov ebx, r14d
	rol ebx, 0xb
	add r8d, eax
	add eax, 0xFFF5271C
	add r8d, r11d
	lea r11d, [rax + r11*2]
	mov eax, ecx
	mov ecx, ebx
	xor ecx, r8d
	xor eax, r11d
	rol eax, 1
	xor eax, r11d
	ror ecx, 2
	xor ecx, r8d
	rol eax, 2
	xor eax, r11d
	ror ecx, 3
	xor ecx, r8d
	rol eax, 3
	xor eax, r11d
	ror ecx, 4
	xor ecx, r8d
	rol eax, 4
	xor eax, r11d
	ror ecx, 5
	xor ecx, r8d
	rol eax, 5
	xor eax, r11d
	ror ecx, 6
	xor ecx, r8d
	rol eax, 6
	xor eax, r11d
	ror ecx, 7
	xor ecx, r8d
	rol eax, 7
	xor eax, r11d
	ror ecx, 8
	xor ecx, r8d
	rol eax, 8
	xor eax, r11d
	ror ecx, 9
	rol eax, 9
	xor ecx, r8d
	xor eax, r11d
	ror ecx, 0xa
	xor ecx, r8d
	rol eax, 0xa
	xor eax, r11d
	ror ecx, 0xb
	xor ecx, r8d
	rol eax, 0xb
	xor eax, r11d
	ror ecx, 0xc
	xor ecx, r8d
	rol eax, 0xc
	xor eax, r11d
	ror ecx, 0xd
	xor ecx, r8d
	rol eax, 0xd
	xor eax, r11d
	ror ecx, 0xe
	xor ecx, r8d
	rol eax, 0xe
	xor eax, r11d
	ror ecx, 0xf
	xor ecx, r8d
	rol eax, 0xf
	xor eax, r11d
	rol ecx, 0x10
	xor ecx, r8d
	rol eax, 0x10
	xor eax, r11d
	rol ecx, 0xf
	ror eax, 0xf
	xor ecx, r8d
	xor eax, r11d
	rol ecx, 0xe
	xor ecx, r8d
	ror eax, 0xe
	rol ecx, 0xd
	xor eax, r11d
	xor ecx, r8d
	ror eax, 0xd
	rol ecx, 0xc
	xor eax, r11d
	xor ecx, r8d
	ror eax, 0xc
	rol ecx, 0xb
	xor eax, r11d
	xor ecx, r8d
	ror eax, 0xb
	rol ecx, 0xa
	xor eax, r11d
	xor ecx, r8d
	ror eax, 0xa
	rol ecx, 9
	xor eax, r11d
	xor r8d, ecx
	ror eax, 9
	mov ebx, r8d
	xor eax, r11d
	rol ebx, 8
	ror eax, 8
	mov ecx, ebx
	xor eax, r11d
	movzx r11d, bl
	shr ecx, 0x18
	mov ecx, dword [r9 + rcx*4]
	xor ecx, dword [rsi + r11*4]
	mov r11d, ebx
	shr r11d, 0x10
	movzx ebx, bh
	movzx r11d, r11b
	xor ecx, dword [r10 + r11*4]
	mov r11d, eax
	xor ecx, dword [rdi + rbx*4]
	shr r11d, 0x18
	movzx ebx, al
	mov r11d, dword [r10 + r11*4]
	xor r11d, dword [r9 + rbx*4]
	mov ebx, eax
	shr ebx, 0x10
	movzx ebx, bl
	xor r11d, dword [rdi + rbx*4]
	movzx ebx, ah
	xor r11d, dword [rsi + rbx*4]
	mov ebx, 0x8FEDB3CE
	add ebx, ecx
	add ecx, 0x0F868EFB4
	add ebx, r11d
	lea r11d, [rcx + r11*2]
	xor edx, r11d
	mov ecx, edx
	mov edx, ebp
	rol edx, 7
	rol ecx, 1
	xor ecx, r11d
	xor edx, ebx
	ror edx, 2
	rol ecx, 2
	xor ecx, r11d
	xor edx, ebx
	ror edx, 3
	rol ecx, 3
	xor ecx, r11d
	xor edx, ebx
	ror edx, 4
	rol ecx, 4
	xor ecx, r11d
	xor edx, ebx
	ror edx, 5
	rol ecx, 5
	xor ecx, r11d
	xor edx, ebx
	rol ecx, 6
	ror edx, 6
	xor ecx, r11d
	xor edx, ebx
	ror edx, 7
	rol ecx, 7
	xor ecx, r11d
	xor edx, ebx
	ror edx, 8
	rol ecx, 8
	xor ecx, r11d
	xor edx, ebx
	ror edx, 9
	rol ecx, 9
	xor ecx, r11d
	xor edx, ebx
	ror edx, 0xa
	rol ecx, 0xa
	xor ecx, r11d
	xor edx, ebx
	ror edx, 0xb
	rol ecx, 0xb
	xor ecx, r11d
	xor edx, ebx
	ror edx, 0xc
	rol ecx, 0xc
	xor ecx, r11d
	xor edx, ebx
	ror edx, 0xd
	rol ecx, 0xd
	xor ecx, r11d
	xor edx, ebx
	rol ecx, 0xe
	ror edx, 0xe
	xor ecx, r11d
	xor edx, ebx
	ror edx, 0xf
	rol ecx, 0xf
	xor ecx, r11d
	xor edx, ebx
	rol edx, 0x10
	rol ecx, 0x10
	xor ecx, r11d
	xor edx, ebx
	rol edx, 0xf
	ror ecx, 0xf
	xor ecx, r11d
	xor edx, ebx
	rol edx, 0xe
	ror ecx, 0xe
	xor ecx, r11d
	xor edx, ebx
	rol edx, 0xd
	ror ecx, 0xd
	xor ecx, r11d
	xor edx, ebx
	rol edx, 0xc
	ror ecx, 0xc
	xor ecx, r11d
	xor edx, ebx
	rol edx, 0xb
	ror ecx, 0xb
	xor ecx, r11d
	xor edx, ebx
	ror ecx, 0xa
	rol edx, 0xa
	xor ecx, r11d
	xor edx, ebx
	rol edx, 9
	ror ecx, 9
	xor ecx, r11d
	xor edx, ebx
	rol edx, 8
	ror ecx, 8
	xor ecx, r11d
	xor edx, ebx
	rol edx, 7
	ror ecx, 7
	xor ecx, r11d
	xor edx, ebx
	rol edx, 6
	ror ecx, 6
	xor ecx, r11d
	xor edx, ebx
	rol edx, 5
	ror ecx, 5
	xor ecx, r11d
	xor edx, ebx
	rol edx, 4
	ror ecx, 4
	xor ecx, r11d
	mov r11d, edx
	movzx ebx, dl
	shr r11d, 0x18
	movzx ebp, cl
	mov r11d, dword [r9 + r11*4]
	xor r11d, dword [rsi + rbx*4]
	mov ebx, edx
	shr ebx, 0x10
	movzx ebx, bl
	xor r11d, dword [r10 + rbx*4]
	movzx ebx, dh
	xor r11d, dword [rdi + rbx*4]
	mov ebx, ecx
	shr ebx, 0x18
	mov r10d, dword [r10 + rbx*4]
	xor r10d, dword [r9 + rbp*4]
	movzx ebx, ch
	mov r9d, r10d
	mov r10d, ecx
	shr r10d, 0x10
	movzx r10d, r10b
	xor r9d, dword [rdi + r10*4]
	rol r8d, 7
	mov edi, r9d
	xor edi, dword [rsi + rbx*4]
	mov esi, edi
	mov edi, 0x91D02C15
	add edi, r11d
	add r11d, 0x167E217B
	add edi, esi
	xor r8d, edi
	ror r8d, 2
	lea esi, [r11 + rsi*2]
	xor r8d, edi
	ror r8d, 3
	xor eax, esi
	xor r8d, edi
	rol eax, 1
	ror r8d, 4
	xor eax, esi
	xor r8d, edi
	rol eax, 2
	ror r8d, 5
	xor eax, esi
	xor r8d, edi
	rol eax, 3
	ror r8d, 6
	xor eax, esi
	xor r8d, edi
	rol eax, 4
	ror r8d, 7
	xor eax, esi
	rol eax, 5
	xor eax, esi
	rol eax, 6
	xor eax, esi
	rol eax, 7
	xor eax, esi
	xor r8d, edi
	ror r8d, 8
	rol eax, 8
	xor eax, esi
	xor r8d, edi
	ror r8d, 9
	rol eax, 9
	xor eax, esi
	xor r8d, edi
	ror r8d, 0xa
	rol eax, 0xa
	xor eax, esi
	xor r8d, edi
	ror r8d, 0xb
	rol eax, 0xb
	xor eax, esi
	xor r8d, edi
	ror r8d, 0xc
	rol eax, 0xc
	xor eax, esi
	xor r8d, edi
	ror r8d, 0xd
	rol eax, 0xd
	xor eax, esi
	xor r8d, edi
	ror r8d, 0xe
	rol eax, 0xe
	xor eax, esi
	xor r8d, edi
	ror r8d, 0xf
	rol eax, 0xf
	xor eax, esi
	xor r8d, edi
	rol r8d, 0x10
	rol eax, 0x10
	xor eax, esi
	xor r8d, edi
	rol r8d, 0xf
	ror eax, 0xf
	xor eax, esi
	xor r8d, edi
	rol r8d, 0xe
	ror eax, 0xe
	xor eax, esi
	xor r8d, edi
	rol r8d, 0xd
	ror eax, 0xd
	xor eax, esi
	xor r8d, edi
	rol r8d, 0xc
	ror eax, 0xc
	xor eax, esi
	xor r8d, edi
	rol r8d, 0xb
	ror eax, 0xb
	xor eax, esi
	xor r8d, edi
	rol r8d, 0xa
	ror eax, 0xa
	xor eax, esi
	xor r8d, edi
	rol r8d, 9
	ror eax, 9
	xor eax, esi
	xor r8d, edi
	xor edx, 0x78ed5f5b
	rol r8d, 8
	ror eax, 8
	xor ecx, 0x9bbb9218
	xor eax, esi
	xor r8d, edi
	mov r9d, edx
	rol r8d, 7
	ror eax, 7
	mov r10d, ecx
	xor eax, esi
	xor r8d, edi
	rol r8d, 6
	ror eax, 6
	xor eax, esi
	xor r8d, edi
	rol r8d, 5
	ror eax, 5
	xor eax, esi
	xor edi, r8d
	xor esi, 0x353265a9
	rol edi, 4
	ror eax, 4
	xor edi, 0xcf7199c3
	xor eax, esi
	mov r11d, edi
	mov r12d, eax
	xor eax, eax
	xor r9d, 0xc5340152
	xor r10d, 0xd0cee4e9
	xor r11d, 0xbbf75dbc
	xor r12d, 0x203c40d7
	or eax, r9d
	or eax, r10d
	or eax, r11d
	or eax, r12d
	mov edx, eax
	xor eax, eax
	nop 
	nop 
	nop 
	nop 
	nop 
	xor rbx, rbx
	inc rbx
	nop 
	cmp edx, 0
	je .ok
	mov eax, 0
	ret
	.ok:
		mov eax, 1
		ret

section .data
tbl1 dd 0x9a7423e5, 0x1b8b132e, 0x3380eb8, 0xc62a44db, 0x522c562e, 0x2871f9f5, 0x4af3752, 0x7421040, 0x2a6f94a4, 0x16912c87, 0xb338155a, 0xf8e1f46f, 0xc4cc8750, 0xab3f4b82, 0x14021957, 0x51f97163, 0xf061e95a, 0x782069d6, 0xc1c6c1cc, 0x695f6966, 0xdcffccf1, 0xca57990d, 0x73600c96, 0x7c39a72f, 0x140a899e, 0xd0e750ca, 0x5700d93d, 0x784423f0, 0x96780ce1, 0xcfec1f58, 0xe7e9f68d, 0xecc98241, 0x70f14d39, 0x9d8ff6e7, 0xce342f63, 0xd125423f, 0xb26a839f, 0xb63a3f0d, 0x97d52418, 0xa4bd33a6, 0x24c56edb, 0x904ae1a, 0x6fc07dc4, 0xc91086ea, 0xb7fa960c, 0xa3085642, 0xbf0f0377, 0xbe07f511, 0x4b6c4baf, 0x5d48f9eb, 0x5b07dd30, 0xde4bfd84, 0x330682f1, 0x61c67c48, 0x2308251d, 0xe76a902e, 0xe3497d2f, 0x86c98be0, 0x9d2ef9dc, 0xe71c86c9, 0xbb3b59e6, 0x4932ee9e, 0xf18d2b6b, 0xf5413f7d, 0xb8198cf9, 0x7b44f445, 0xc1d25a4c, 0x9d45087a, 0xaf63d6c8, 0x844e7ab9, 0x79b11dac, 0x8425cdfd, 0x6e99fbad, 0x739cbb34, 0xe9d3b0e0, 0x4e8f181c, 0x48d41f5f, 0x45f6d685, 0x8654b625, 0x873750c3, 0xf497e98f, 0x23161623, 0x4d465f43, 0x2d9e5ce2, 0x2a9d5636, 0x266e7cc8, 0x6b450869, 0x52eae1bd, 0x837d1ca5, 0x409928ad, 0xcae5e387, 0x705a75a3, 0xead3dbd7, 0x9c425cde, 0x1b382ca2, 0x150a0f6b, 0x7d580ff9, 0x147d53a1, 0xa923d301, 0x577e251a, 0x4253dcd2, 0x49aabeb4, 0x5ba26e83, 0x2403e6d2, 0x7aab2b9b, 0x2b666686, 0xe8e40978, 0x49948aa0, 0xbda4f3e0, 0x95ac1a20, 0x206a12f1, 0x1392fc4d, 0x7c5992a7, 0x5dc9cf6a, 0x53dd3984, 0xb5f2b381, 0x934adf1a, 0x95602001, 0x4c0aef1a, 0x5f9fe14f, 0x9716fb0b, 0xdb3557e2, 0xdfba3bae, 0x67c7f910, 0x8a257f15, 0xe270cc2, 0x710b1b38, 0x114bec47, 0xebc28b71, 0x8b3bcb23, 0xce99e2dc, 0xb08faffb, 0x1de96c2c, 0xf85fa295, 0x936aa6e0, 0x756e7171, 0x19ef835e, 0xf436efba, 0xcee93432, 0x2ab123ea, 0x9a30fe60, 0x8d129cc8, 0x86bdfac4, 0xcb42c44a, 0x3c020694, 0x39ba8e49, 0xdca02f4e, 0x58592124, 0xadf0554c, 0x986d3d35, 0xccbdda4d, 0xe0036c7d, 0x9e801be, 0xebd4bb08, 0xb8beef9a, 0x8fe02586, 0x6137aff, 0x980e3545, 0x1fac51e0, 0xd46c1e8, 0x8cd67a28, 0xb8808897, 0x908efd1e, 0x84a89f9e, 0x8929524a, 0x30078e4b, 0x35236943, 0xcf287ef4, 0x5efee3e8, 0x3f1d5959, 0xd4e5a329, 0x282ca589, 0xb9e0cf6a, 0x3325a40c, 0x1ec2a4f9, 0xc0a66986, 0x72991057, 0xdee1d642, 0xcf777dbb, 0x6ca1350f, 0x14770154, 0xb5983368, 0x290a646f, 0x44f78f29, 0x777c30b, 0x7d5fbf9b, 0xa20be2b9, 0xe6fb9ac3, 0xb101cb03, 0xc823afd2, 0x92759cb8, 0x2c21bee6, 0xb5310f0e, 0x1c86e553, 0x16361e2a, 0xba2fde2f, 0x323ece5b, 0x7467cf0a, 0xc85413fa, 0x3bef5092, 0xc052179c, 0xa926369b, 0x9d181328, 0x9d399835, 0x42d2da3e, 0x4f4d548, 0x20afc309, 0xaee1c9a, 0xf151b0ef, 0xb4d52972, 0xbc182722, 0x8d361210, 0xea4a38b2, 0x95fa4fe8, 0x324dc72a, 0xc3297174, 0x726353da, 0xd0232411, 0x2c0ffe28, 0xf27dd88d, 0xccaf4060, 0x9b52db6, 0x86366f42, 0x22e5253, 0xb3a5f5c8, 0xf247a7c7, 0xe394b888, 0xa7a12c71, 0x600ee571, 0x5929936b, 0x962357c0, 0xa2a0ab6b, 0xf375eaef, 0x3015ae0d, 0xe7560dc0, 0x5608f651, 0xf4a87a85, 0x7846b7d7, 0x837580f5, 0x5a91fbb0, 0xf749bacf, 0x5a591d04, 0x7a1fba94, 0xc72949ad, 0x2678bd52, 0x392233d8, 0x513935cb, 0x3069be42, 0xe83d6c4f, 0x1d60b4c6, 0x3acdc927, 0xbca945db, 0xfb3ed00, 0xaf4ff569, 0xde3fcde, 0x95321405
tbl2 dd 0xadaca9e7, 0x68edfdb3, 0xcdd90f92, 0x1aecf364, 0xafd0f0d8, 0x1ba992a, 0xee79623a, 0x579c1177, 0x964a1d33, 0x60843973, 0xac4a18e0, 0xc026eccc, 0xb9cc34bc, 0x3b52870e, 0x631ba9b, 0xa33094e, 0x2bb4c35d, 0x54d61672, 0xc57d5164, 0xc10e9c3b, 0xb0877a83, 0x56443482, 0x414f2298, 0xa1b9634, 0xe50034f5, 0x562855e0, 0x6ced4529, 0xe6d1bcf5, 0xd43e494e, 0x6099c93c, 0xc9126e43, 0xe3db1e80, 0xa1dfb9df, 0x2a3b418e, 0x6088d194, 0xe981766c, 0xb21ef054, 0x6736c461, 0x3bb57022, 0x551cf51, 0xe9cc320, 0x6a11898, 0x2184de2c, 0x5ba99f72, 0x9f20f2f3, 0x1fe2a5e, 0xd4069fe5, 0xd0ddf35f, 0xac767e34, 0x7d80519f, 0x41a08bcf, 0xe4dc7acb, 0x6c8b439c, 0xc7ee72e1, 0x25c7f72, 0x3d40942c, 0x9624d293, 0xd71f25e8, 0x35d2bee, 0xe5f25508, 0xbba48b7d, 0xad94c309, 0xa017ec21, 0x7a729d8c, 0x85220bba, 0x9b28a8c9, 0xb6471dc3, 0x4a277c40, 0x6202c7bf, 0x6f5a0c55, 0xf3706e88, 0x51cf190f, 0xb6219ded, 0x8d607c32, 0x876fef6e, 0x70ea4e70, 0xf6e2f4f8, 0x12cec8ba, 0x2c805448, 0xca9036c7, 0x37fa1ef6, 0x11db5ef4, 0xd89b57b5, 0xad25fb64, 0xe39f2565, 0x1b928f25, 0xa2045e5c, 0x312baa06, 0x1e346674, 0xda9375e6, 0x24b236de, 0x516c6dcf, 0xde236eda, 0x84b064a0, 0x789e8397, 0x699a988, 0x67b04aae, 0xb84691e8, 0x7cadee25, 0x592be485, 0xdd3df91d, 0xe7a159d4, 0xf461f373, 0x43ad8008, 0x1a8ccdd2, 0x53aa11a8, 0xa8f8dc4e, 0x7476d69a, 0xcd8def5e, 0x12bb3d87, 0x788e7217, 0xa1b0ade7, 0xbf743336, 0x298d2cff, 0xa842e7bb, 0x5252c495, 0x2d8fe517, 0xeb7b0919, 0xfb5bba42, 0xe3dc9001, 0x75ebe91f, 0xc3e95240, 0x88c6df23, 0x9d55e2f2, 0x59446d2c, 0xbb87b9c2, 0xdd27264c, 0x68926ffa, 0x7733396a, 0x69b9da8e, 0x5cfdc003, 0x57ac8ca4, 0xe735b75d, 0xc92a8df0, 0xa85904fb, 0x5e6469e6, 0xadb4e838, 0xe21cf74, 0x8c1b16e8, 0xd92dd626, 0x518180be, 0xf7f58463, 0x6749890d, 0xfece7cc6, 0xe028b83a, 0x672ce7ad, 0xad1637e3, 0x774af3d0, 0x82e00860, 0x7446d544, 0xfaed9297, 0x7f9f7a92, 0x4dff7260, 0xefea6a65, 0x791ccec1, 0x96e03c74, 0x899610f7, 0xdb5a2ac3, 0x33d90f93, 0xe91c1927, 0x83211691, 0x809e5c40, 0xd540119c, 0x72935ff3, 0x16221ed2, 0xc3e9049a, 0xb48890dc, 0x31f7f722, 0xa9ad9762, 0xa39fe13, 0xc8fd8c78, 0x77454a69, 0x2c499464, 0x5e71358f, 0xb6a2f0a0, 0xf70c913b, 0xc69363b6, 0xd500eb28, 0x53ee2d37, 0x1bf56e95, 0x99852e5, 0x7f2e26bf, 0xeec8d577, 0xaa30dfa2, 0xbe6fd009, 0x7092eacd, 0xde640fa8, 0xca49df5d, 0xdb0ce4ca, 0x59bdde9, 0x83a9b4cf, 0xc9913ffa, 0x860cecf8, 0xe08649a4, 0xc7d8fc6f, 0xd5ff582, 0x4d8a07a9, 0x29baec67, 0xb69b8329, 0xa7e1b80e, 0x2f4d7cd, 0xb687ad89, 0x92de7c32, 0xf7c0d5f9, 0xfb48a4f4, 0xf1bc0d27, 0xf5a337db, 0xba9c35a6, 0x61a2cf73, 0x5b6b7638, 0xc42c51ff, 0x27d3b365, 0xebb2ab4a, 0x9b6f47cd, 0xe14f03a3, 0xa367e034, 0xddd03da8, 0xc2d7524, 0x7312a79d, 0x25e499e2, 0x847abc2b, 0x85b3d680, 0x9adaf83c, 0x1a7eb491, 0xab7fb168, 0xca8f877, 0xc0e0a94a, 0xb546bbc2, 0x3b9be526, 0x895d3dcb, 0x961662c5, 0x2dbb56e3, 0xf575f2e5, 0x4f55efba, 0x93da78f9, 0xaf9d88de, 0xb06a6991, 0xfb761a9, 0xd99a27c3, 0xfec239ad, 0xb3656134, 0x6e387395, 0x913f0c51, 0xec90f54e, 0xfa7a457f, 0xa0d764f, 0xaae08f61, 0x604d6511, 0xb34b0a8b, 0x89a74f89, 0x5675acdd, 0x737afa11, 0x3cb32763, 0x71008593, 0x80cf4c31, 0xca2e9b2c
tbl3 dd 0x1216799e, 0x815ce178, 0xe96b8725, 0xf144a66f, 0x12800d90, 0x8d596187, 0xda7b115e, 0x7a12fe58, 0xfc743fb3, 0xdcb5559f, 0xc1d1e242, 0x8bf8fc13, 0xc62e4dd0, 0x98ef1690, 0x8883e50, 0x8f352efb, 0x527141e0, 0x8b090e77, 0x3a9fff17, 0x52fb7989, 0x35a3ee6c, 0x37b2f189, 0xa663acc0, 0xf9814a98, 0xae312b8d, 0x554f3c1f, 0xdfae0806, 0x6beb1f7a, 0xfef42500, 0x142698e1, 0x5397e99f, 0x67a66348, 0xb6a56da5, 0x96a16d9e, 0x66b96df8, 0x1e4e4ef6, 0xe786cbea, 0xa1880f9c, 0x9a479068, 0xd6fd8a0b, 0x9dbb00d, 0x9c004e5d, 0x430e27ec, 0xa20d25d8, 0x9d6959be, 0x6474ba85, 0x872a81c6, 0x87c5bdb5, 0x4b9a2639, 0x87d1e58c, 0x56a68e67, 0xeb757586, 0x7f62ac5c, 0x71c17412, 0x884f8f74, 0x27d26943, 0xdff7dfbe, 0x75ba41e0, 0xaa31dffa, 0xfb0e5990, 0x4f9beafa, 0x4628e39d, 0x503ed99, 0x10db95aa, 0x3b972a0f, 0x27f31e78, 0x281441d8, 0xb37b4df1, 0x8fc60512, 0x4b747bb4, 0xaf206a2f, 0x38565c8b, 0x587eea83, 0xc5dc516e, 0xc7900708, 0x7a44696f, 0x65d25905, 0xd5461ea0, 0x553fcc6c, 0xd169b578, 0x536c1fc5, 0xab6b5379, 0x3b5ac81c, 0x831ef83f, 0x3a448a1a, 0x66ffa1d7, 0xe19ac3dd, 0xf2c77bff, 0x7846eb2, 0xccda351c, 0x532a4f0a, 0x8894f1b4, 0x5f821872, 0x489ee931, 0x4b0276c8, 0x95c40e79, 0x41a3296d, 0x9327fb9f, 0xf3bc5176, 0x9827d5f5, 0x424e1136, 0x31906a86, 0x9214a0c5, 0xd68fce50, 0xc762d79d, 0xac318ebe, 0xc2ad5e4a, 0xb24a6be9, 0x4ef54fcf, 0x263a388a, 0xb6d8dc0e, 0xf7143220, 0x3c37f48c, 0x82e88fa4, 0x716e63fa, 0xfcdafd47, 0x92d4be43, 0xf71d9688, 0xd13e4a09, 0xdaaadf2c, 0x8a457e25, 0x24df4f61, 0x728a8626, 0xa648e980, 0x88f7370c, 0x570945a0, 0xdc47c72a, 0xba45e4d8, 0x2b53a156, 0x72c1828a, 0xc789b7a, 0x64ac216, 0xe2f8d049, 0x57de12e8, 0x77ec6755, 0xba978ed3, 0x59ceb5d2, 0x9244377f, 0x8c28278a, 0x70f434e4, 0x8ff4b2a, 0xe9504598, 0xefdf62c0, 0x1706ac78, 0x3013ea41, 0x279e9ba6, 0x1ac25849, 0xd912697d, 0xd00a68a8, 0x921a5035, 0x97293d2c, 0xfa3eb4c3, 0xdee50d8d, 0x24b7251e, 0x8e3d7218, 0x82fd31ed, 0x192d7330, 0x2c5f06a7, 0x81031935, 0x7110cb3a, 0x59693faf, 0x6e199099, 0xda9e914c, 0x451c9bfb, 0x57adf60d, 0x8ee43a66, 0x35013213, 0x59ba5c18, 0xdc85af7a, 0x6d46c34, 0x8439704c, 0x71f8bbf4, 0x3bb496d9, 0xe73c84ac, 0x22046526, 0x80859fc9, 0xaeec76b1, 0xacdd19bd, 0xda9ef1cc, 0x6293559d, 0xe4ad84fa, 0x1fa1902a, 0xb1b4ad9f, 0xfa746645, 0x3553c08, 0x581dee6b, 0xed6a94eb, 0xb7ecfddd, 0xb562d8d, 0x931a5f31, 0x24a0b94, 0xaf1af2bb, 0x4ecda9e, 0xa7e2e626, 0xd854bb39, 0x35eaf600, 0x23e7a418, 0x15b38033, 0x2e8ab877, 0x1bd4e609, 0xa139e376, 0x2ee0a007, 0x651bea6d, 0x7cf0c7b7, 0x78b49df4, 0x663e5fb5, 0x9eb720c8, 0x2ea2d578, 0x77f4a0a2, 0xad8448c2, 0x1f1590f2, 0x48251cd4, 0xb4f3e73b, 0xf03b06cf, 0xbe5e2f05, 0x5d87a2a0, 0x1a71ceba, 0x95fc9740, 0x86b28a44, 0x25f6c328, 0xe53b717d, 0xfdceb5fa, 0x7faa054d, 0xb43a835a, 0xfccc85b9, 0xb610a4ed, 0xcc174e3e, 0xc8d60a8d, 0x6a02a212, 0x93f9c924, 0x59f61f55, 0x33b23f87, 0x77c082bd, 0x8c50d933, 0x7a951ecc, 0x6c29b84b, 0xeac44fc, 0xb9a337d8, 0xe9024426, 0xc5f3d25d, 0x384374f9, 0x3d1d8cd8, 0xae97d876, 0x57806af2, 0x74eb42f7, 0x2cd8a486, 0x39729a1a, 0xf6615ea3, 0xb4771d70, 0x4a426449, 0x36f91408, 0x90d64991, 0x8332eac3, 0x67765eb0, 0x1009c26e, 0x35c84c55
tbl4 dd 0x4f8da321, 0xbe0f3555, 0xcc9c69a3, 0x2d5f5938, 0x874ad66a, 0x8b36b7bd, 0x3e41f478, 0xf0e8682d, 0xe4173bb6, 0x538b313d, 0xc509a84e, 0xf16fae15, 0x312ad0f, 0xd3609013, 0x7444a978, 0x6783f320, 0x368b8803, 0x1036dbbb, 0xac1a9e1f, 0x73861d30, 0x1e6264de, 0x92a0a7bb, 0x834b3dac, 0xe5af4c79, 0x75e5ace, 0xd56a1c26, 0x87de1db7, 0x81d95ab0, 0xcfb4ff21, 0xbf6ec0a4, 0x2cb058cc, 0x48f2a3c8, 0xa416c94, 0xf4576d79, 0xf102e822, 0x7e83892, 0xd646f914, 0x6e453e8d, 0xd98ff2d2, 0xf1be15b7, 0xb16a119d, 0x9bce3b9f, 0xfd79aba8, 0xfb1b75b9, 0x79d5cda2, 0x36b66f51, 0x5a5c415b, 0x842c7c25, 0xce4d32a5, 0x77ee339, 0xd9b550cb, 0xd9af247e, 0x58400da, 0xd28a5783, 0x5ac33b7, 0x7ed7f9e4, 0x480a914f, 0x38691cc, 0x661372ec, 0xddaa1a54, 0xcd311019, 0xc60f823e, 0x66893591, 0x6d9fbf12, 0x6ba81702, 0x1ad5306f, 0xca4b828, 0x447e2faf, 0xc9344c91, 0x31dc1708, 0x6a9056d4, 0xe0f21536, 0xf93eb4b9, 0x9cce2509, 0x70ef90f6, 0x833ab936, 0x56a10b35, 0x93020d36, 0xc1a305d5, 0xcdaaf4f4, 0x4522c53c, 0xa9775fba, 0x5647e8a8, 0x91e766f0, 0x336f12e8, 0x1d5779bd, 0x3594f54b, 0x74a6e10, 0x63085e81, 0x42eda61d, 0x91a4b28b, 0x9a4f091a, 0x9d077c89, 0x8509b4ed, 0x8fd060f9, 0xb7afbeaf, 0xe770962, 0x4cbf6e61, 0x679865fa, 0x6210ec58, 0xbc08c240, 0xfdb176cf, 0x85abbf4c, 0x99ccde1b, 0x471f1379, 0xbb524dd9, 0xa9b3161d, 0x98ab4ca2, 0xc06a7cb2, 0xbd331a, 0xd6994ab9, 0x485159eb, 0x72982563, 0x91394bda, 0x5ecf5767, 0x8576fbb2, 0x188754f4, 0x38d2b487, 0xc97f0562, 0x365f6531, 0x8f0f5682, 0x65482530, 0xe11302ca, 0xcacc7493, 0xbc8f2749, 0x6a9bda0a, 0x4df42de2, 0xa48bb40e, 0x683f680d, 0x6839bad2, 0x17be71ba, 0x3d6cd6d9, 0x5a43097f, 0xbf0d62df, 0x6da6160, 0xf5bcc73f, 0x782f161b, 0x15d64f81, 0xe512b3d9, 0xc9d83dc5, 0x810dc766, 0x39c375b1, 0xe95cdc5a, 0xb6da7253, 0xe2130de6, 0xc561b7da, 0x638367d2, 0x293bc15b, 0xdf6fccfd, 0xca65b4da, 0x74a806e4, 0x50926fba, 0x6e1b1e58, 0x3b13ea39, 0x9810f404, 0xe8e271d4, 0xf2249213, 0xfe465d67, 0xf1b65f7e, 0x27340632, 0xbcd110d0, 0x7f22ec57, 0x761442c1, 0xa29845fa, 0x6890c548, 0x83ece32c, 0xb54b150, 0x2d66dc08, 0x14cdb30f, 0xb4fa5af9, 0xf40d4a8a, 0xcb86c52f, 0xfe8e6fe3, 0xbd4743b9, 0x3aff6c9a, 0x9b2de736, 0x2b53b1b7, 0xd7a1df72, 0xa82b0af4, 0x1363691c, 0xdcb3afb9, 0xb3a19f08, 0x9f8479b5, 0xbade9e5d, 0x6e4898ff, 0x7f4b9fb5, 0xe87ea1d3, 0x32f05ae, 0x7f83ff00, 0xd4654a88, 0x2f082eae, 0xf23e4ce, 0xd9fd2649, 0xb35c0c1c, 0x5d7fba5c, 0x77898f0c, 0x274e15c7, 0xa249b69b, 0x2e381d24, 0x3cc6040c, 0x6b170005, 0x2957e6c4, 0x4d84bbbf, 0x7f873058, 0xa8bdc918, 0xce74bb75, 0x3081a7a6, 0xa8c4fb9f, 0x25d19477, 0x72e9c814, 0xca68d0cc, 0xd66b0c49, 0x373f0cf4, 0x7ef16cf8, 0x116da03c, 0x9ee7797b, 0x4495fff1, 0x3fdaa0e4, 0xa23e1de9, 0xd91f1b6b, 0x9c5a7717, 0xe31f7496, 0xbfb228b5, 0x87ea5ecc, 0xf99a662b, 0x697ae38d, 0x4c755e35, 0x72a9d241, 0x2b202dbe, 0x6f531370, 0x565d5ab4, 0x9f56097f, 0x8e323fb1, 0xe5bc8216, 0xf47fe454, 0x43b6bdbb, 0x4452ab9f, 0x355ef752, 0xe8b5f010, 0x5422fe68, 0xb5e45e82, 0xfea6b471, 0x7c99aab6, 0xd2cf3117, 0x3a53efc9, 0x64e35cbd, 0xc11af678, 0x3da6ed3, 0x57a2e327, 0xf4caf99d, 0xa06d23c9, 0xd0a86d09, 0xca156176, 0x839d1e69, 0xb3c3aca4, 0xfb5078de
inp dd 0x41424344, 0x45464748, 0x494a4b4c, 0x4d4e4f50
