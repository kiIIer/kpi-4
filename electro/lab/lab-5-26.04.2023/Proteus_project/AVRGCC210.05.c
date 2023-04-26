#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>
#define F_CPU 16000000L
int main(void) // 0
{
	// 1: Init port B
DDRB = 0b00100011;
PORTB= 0b00000000;
// 2: Init 16-bit timer 1 values
OCR1A = 20;
ICR1 = 40;    
int delay = 1;

	// Init Phase and frequency correct PWM
TCCR1B = _BV(WGM13);  // 3
TCCR1A = 0;
TCCR1A |= _BV(COM1A0);// 4
TCCR1A |= _BV(COM1A1);
TCCR1B |= _BV(CS11);  // 5


char flag_start_stop=0,flag_reverse=0,flag_speedup=0,flag_speeddown=0;

while(1) // 6
	{
	// 7: Start-Stop button action
if(!(PINB&4))
{ flag_start_stop=1; _delay_ms(10); }
if(( flag_start_stop==1 )&&(PINB&4))
{PORTB^=1; flag_start_stop=0; } 	// 8

// 9: Reverse button action
if(!(PINB&8))	
{ flag_reverse=1; _delay_ms(10); }
	if(( flag_reverse==1 )&&(PINB&8))
{PORTB^=3; flag_reverse=0; } 	// 10

// 11: Speed - button action
if(!(PINB&16))	
{ flag_speeddown=1; _delay_ms(10); }
if(( flag_speeddown==1 )&&(PINB&16))
{ if (OCR1A!=40) OCR1A+=delay; flag_speeddown=0; } // 12

// 13: Speed + button action
	if(!(PINB&64))
{ flag_speedup=1; _delay_ms(10); }
if(( flag_speedup==1 )&&(PINB&64))
{ 
	if (OCR1A!=0)OCR1A-=delay; // 14
flag_speedup=0; 
	}
} // 6: End of loop
} // 15: End of proram
