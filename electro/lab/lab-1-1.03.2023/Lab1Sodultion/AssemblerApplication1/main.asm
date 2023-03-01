;
; AssemblerApplication1.asm
;
; Created: 3/1/2023 8:30:19 AM
; Author : killer
;


; Replace with your application code
start:

; �������� 1A ������/˳������� ������������ ��������� 4782D
ldi	r17,0x47
ldi	r16,0x82
out	TCNT1H,r17
out	TCNT1L,r16

in	r18,TCNT1L
in	r19,TCNT1H

; �������� 1B �������� ���� ������� R2 � ������ R3 ��� ������� mov
ldi r17, 2
clr r2
add r2, r17

ldi r17, 3
clr r3
add r3, r17

clr r3
add r3, r2

; �������� 1C ���� ������� 5-7 �������� � ���� ���������� ����������� ������� ����� �� ������� AF
ldi r16, high(0xAF)
out SPH, r16
ldi R16, low(0xAF)
out SPL, r16

ldi r16, 5
mov r5, r16

ldi r16, 6
mov r6, r16

ldi r16, 7
mov r7, r16

push r5
push r6
push r7

; �������� 2� ���� PORTB � PORTC ������ � �������� �� ������� 70h � ������������� ������
in r16, PORTB
in r17, PORTC
add r16, r17
sts 0x70, r16

; �������� 2B, ������ ���������� �����, �� ����������� � �/�1 � ��������� �����: ����������� � ���� �������� ��������
in	r17, TCNT1H
in	r16, TCNT1L
ldi r18, 1
ldi r19, 2

add r16, r18
adc r17, r19

; �������� 2C ³����� � ����������� �����, ������������� � R23, R24, ����� 34DEh, ���������� ������� �������������� �������
ldi r23, 123
ldi r24, 222

com r23
com r24

subi r23, 0xDE
sbci r24, 0x34

; ����� �� ������������ 3 ��� � ������� �� � ������������� ������ �������� � ������ ������� ������� R22.

mov r23, r22

andi r23, 0b00000111

lsl r23
lsl r23
lsl r23
lsl r23
lsl r23

ld r24, Z

andi r24, 0b0000001

lsl r24
lsl r24
lsl r24

or r23, r24

mov r22, r23

; ���������� ������ ������� r13 = not(bit1 * PORTC) * not(r25)

in r16, PORTC

ld R17, Z

and r16, r17  
com r16       
mov r18, r16

mov r19, r25

com r19        
mov r20, r19

and r18, r20
mov r13, r18

;���������� ������� ������ � ������� 4.5.

ld r16, Z