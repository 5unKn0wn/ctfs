; assemble using pwntools
mov rsi, 0x20000
call transform
mov rdi, rax
call f_evaluate
mov rsi, 0x24300
mov rdi, rax
call transform
mov r10, rax
mov rdi, r10
call verify_parity
test rax, rax
jz rejected
and r10, 0xfffff
cmp r10, 0xE17A3
jnz rejected
xor rax, rax
inc rax
jmp end

transform:
	xor rbx, rbx
	xor r8, r8
	jmp loc_763

	loc_701:
		lea rdx, [r8 * 8]
		mov rax, rsi
		add rax, rdx
		mov rax, [rax]
		and rax, rdi
		mov rbp, rax
		xor r9, r9
		jmp loc_740

	loc_72A:
		mov rax, rbp
		and eax, 1
		xor r9, rax
		mov rax, rbp
		shr rax, 1
		mov rbp, rax

	loc_740:
		test rbp, rbp
		jnz loc_72A
		mov rax, 0x3f
		sub rax, r8
		mov rdx, r9
		mov rcx, rax
		shl rdx, cl
		mov rax, rdx
		or rbx, rax
		inc r8

	loc_763:
		cmp r8, 0x3f
		jle loc_701
		mov rax, rbx
		ret

f_evaluate:
	xor rbx, rbx
	xor rsi, rsi
	xor rbp, rbp
	inc rbp
	jmp loc_6D8

	loc_66A:
		mov rax, rbp
		mov r8, rax
		jmp loc_6CE

	loc_672:
		mov rax, 0x40
		sub rax, rbp
		mov rdx, rdi
		mov rcx, rax
		shr rdx, cl
		mov rax, rdx
		and rax, 1
		test rax, rax
		jz loc_6C6
		mov rax, 0x40
		sub rax, r8
		mov rdx, rdi
		mov rcx, rax
		shr rdx, cl
		mov rax, rdx
		and rax, 1
		test rax, rax
		jz loc_6C6
		mov rax, rsi
		cdqe
		lea rdx, [rax * 8]
		mov rax, 0x20200
		mov rax, [rdx + rax]
		xor rbx, rax

	loc_6C6:
		inc rsi
		inc r8

	loc_6CE:
		cmp r8, 0x40
		jle loc_672
		inc rbp

	loc_6D8:
		cmp rbp, 0x40
		jle loc_66A
		mov rax, rbx
		ret

verify_parity:
	mov rax, rdi
	and rax, 0xfffff
	mov rbx, rax
	mov rax, rdi
	shr rax, 0x14
	mov rsi, rax
	xor rbp, rbp
	xor r8, r8
	jmp loc_7CF

	loc_7A1:
		mov rax, r8
		mov rdx, rbx
		mov rcx, rax
		shr rdx, cl
		mov rax, rdx
		and rax, 1
		test rax, rax
		jz loc_7CB
		mov rax, r8
		mov rdx, rsi
		mov rcx, rax
		shl rdx, cl
		mov rax, rdx
		xor rbp, rax

	loc_7CB:
		inc r8

	loc_7CF:
		cmp r8, 0x13
		jle loc_7A1
		mov r9, 0
		jmp loc_817

	loc_7DE:
		mov rax, 0x3f
		sub rax, r9
		mov rdx, rbp
		mov rcx, rax
		shr rdx, cl
		mov rax, rdx
		and rax, 1
		test rax, rax
		jz loc_813
		mov rax, r9
		mov rdx, 0xBD1EE46C30800000
		mov rcx, rax
		shr rdx, cl
		mov rax, rdx
		xor rbp, rax

	loc_813:
		inc r9

	loc_817:
		cmp r9, 0x17
		jle loc_7DE
		cmp rbp, 1
		setz al
		movzx eax, al
		ret

rejected:
	xor rax, rax
end:
	xor r10, r10
