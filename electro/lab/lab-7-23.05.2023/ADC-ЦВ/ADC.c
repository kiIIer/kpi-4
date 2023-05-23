// ??????????? ?????????? ?????? ?????????
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

// ????? ??????? ??? ???????????? ???? ?? ?????????????? ???????????
//-------------0-----1-----2-----3-----4-----5-----6-----7-----8------9----dp
char SEG[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F,0x67};
char SEG_with_dot[] = {0xBF,0x86,0xdB,0xCF,0xE6,0xED,0xFD,0x87,0xFF,0xEF,0xE7};

// ????????????? ?????????? ???????
volatile unsigned char current_indicator = 0;
volatile unsigned int display = 0;
volatile unsigned int ADC_value;
// ???? 1 - ????????????? ????????
int main (void)
{
    // ???? 1.1 - ????????? ?????? ?????????????? ???????????
    DDRC = 0xFF;
    PORTC = 0x00;
    DDRD = 0xFF;
    PORTD = 0x00;

    // ???? 1.2 - ???????????? ??????? 2
    TIMSK |= (1 << TOIE2); // ?????? ??????????? ?? ??????? 2
    TCCR2 |= (1 << CS21);  // ???????????? ?? 8

    // ???? 1.3 - ???????????? ???
    ADCSRA |= (1 << ADEN) // ?????? ???
    |(1 << ADSC) // ?????? ????????????
    |(1 << ADATE) // ??????????? ????? ?????? ???
    |(1 << ADPS2)|(1 << ADPS1) // ???????????? ?? 64
    |(1 << ADIE); // ?????? ?????????? ??? ???

    ADMUX &= (~(1 << REFS1))&(~(1 << REFS0)); // ???????? ???
    
    // ???? 1.4 - ?????????? ?????? ??????????
    sei();

    // ???? 1.5 - ???????? ????
    while(1)
    {
       _delay_ms(50); // ???????? 50 ??
    }
}

// ???? 2 - ????? ??????????? ??? ???
ISR (ADC_vect)
{// ???? 3 - ???????? ??????????? ??? ???
	display = (ADC+1)*(5/1024.0)*100;
}

// ???? 4 - ????? ??????????? ??? ??????? ?2
ISR (TIMER2_OVF_vect)
{// ???? 5 - ???????? ?????????? ??? ??????? ?2
    PORTD = 0xFF; // ????????? ??? ????????
    PORTC = (1 << current_indicator); // ???????? ???????? ?????????
    switch (current_indicator)
    {
        case 0:
        PORTD = ~(SEG[display % 10000 / 1000]); // ???????? ????? ????????
        break;
        case 1:
        PORTD = ~(SEG_with_dot[display % 1000 / 100]); // ???????? ????? ??????? ?? ??????
        break;
        case 2:
        PORTD = ~(SEG[display % 100/10]); // ???????? ????? ???????
        break;
        case 3:
        PORTD = ~(SEG[display % 10]); // ???????? ????? ?????
        break;
    }
    if ((current_indicator++) > 2) // ?????????? ?? ????????? ?????????
        current_indicator = 0; // ?????????, ???? ??? ?? ??????
}
