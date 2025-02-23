	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 1
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3, 0x0                          ## -- Begin function calcular_area
LCPI0_0:
	.quad	0x400921fb54442d18              ## double 3.1415926535897931
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_calcular_area
	.p2align	4, 0x90
_calcular_area:                         ## @calcular_area
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movsd	%xmm0, -8(%rbp)
	movsd	LCPI0_0(%rip), %xmm0            ## xmm0 = mem[0],zero
	mulsd	-8(%rbp), %xmm0
	mulsd	-8(%rbp), %xmm0
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3, 0x0                          ## -- Begin function main
LCPI1_0:
	.quad	0x4008000000000000              ## double 3
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	movl	$0, -4(%rbp)
	movsd	LCPI1_0(%rip), %xmm0            ## xmm0 = mem[0],zero
	movsd	%xmm0, -16(%rbp)
	movsd	-16(%rbp), %xmm0                ## xmm0 = mem[0],zero
	callq	_calcular_area
	movsd	%xmm0, -24(%rbp)
	movl	$2, -28(%rbp)
	movsd	-24(%rbp), %xmm0                ## xmm0 = mem[0],zero
	cvtsi2sdl	-28(%rbp), %xmm1
	mulsd	%xmm1, %xmm0
	movsd	%xmm0, -40(%rbp)
	movsd	-16(%rbp), %xmm0                ## xmm0 = mem[0],zero
	movsd	-24(%rbp), %xmm1                ## xmm1 = mem[0],zero
	movl	-28(%rbp), %esi
	movsd	-40(%rbp), %xmm2                ## xmm2 = mem[0],zero
	leaq	L_.str(%rip), %rdi
	movb	$3, %al
	callq	_printf
	xorl	%eax, %eax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Radio: %.2f\nArea: %f\nMultiplicador: %d\nResultado: %f\n"

.subsections_via_symbols
