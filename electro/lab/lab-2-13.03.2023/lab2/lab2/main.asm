;
; lab2.asm
;
; Created: 3/13/2023 10:54:05 PM
; Author : killer
;

LDI R16, 0x1F
CP R19, R16
BRCS L1

IN R21, SREG
RJMP L2

L1:
IN R22, SREG

L2:

ldi r22, 22
ldi r23, 23
ldi r24, 24

IN R16, SREG

SBRC R21, 0          
RJMP COPY_SEQ_1


    MOV R12, R22
    MOV R13, R23
    MOV R14, R24
    RJMP COPY_SEQ_END

COPY_SEQ_1:
    MOV R22, R12
    MOV R23, R13
    MOV R24, R14

COPY_SEQ_END: