	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 1
	.globl	_main                           ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movl	$0, -4(%rbp)
	movl	$5, -8(%rbp)
	movl	$10, -12(%rbp)
	leaq	L_.str(%rip), %rdi
	leaq	L_.str.1(%rip), %rsi
	movb	$0, %al
	callq	_printf
	movl	-8(%rbp), %eax
	movl	%eax, -20(%rbp)                 ## 4-byte Spill
	movl	-12(%rbp), %eax
	movl	%eax, -16(%rbp)                 ## 4-byte Spill
	movl	-8(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jle	LBB0_2
## %bb.1:
	movl	-8(%rbp), %eax
	movl	%eax, -24(%rbp)                 ## 4-byte Spill
	jmp	LBB0_3
LBB0_2:
	movl	-12(%rbp), %eax
	movl	%eax, -24(%rbp)                 ## 4-byte Spill
LBB0_3:
	movl	-16(%rbp), %edx                 ## 4-byte Reload
	movl	-20(%rbp), %esi                 ## 4-byte Reload
	movl	-24(%rbp), %ecx                 ## 4-byte Reload
	leaq	L_.str.2(%rip), %rdi
	movb	$0, %al
	callq	_printf
	leaq	L_.str(%rip), %rdi
	leaq	L_.str.3(%rip), %rsi
	movb	$0, %al
	callq	_printf
	xorl	%eax, %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"DEBUG: %s\n"

L_.str.1:                               ## @.str.1
	.asciz	"Iniciando el programa."

L_.str.2:                               ## @.str.2
	.asciz	"El m\303\241ximo entre %d y %d es %d\n"

L_.str.3:                               ## @.str.3
	.asciz	"Programa finalizado."

.subsections_via_symbols
