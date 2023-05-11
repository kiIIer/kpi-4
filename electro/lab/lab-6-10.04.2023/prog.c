// Підключення заголовних файлів бібліотек
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
char SEG[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07,
              0x7F, 0x6F, 0x80};
volatile unsigned char current_indicator = 0;
volatile unsigned int display = 0;
int main(void)
{
    DDRC = 0xFF;
    PORTC = 0x00;
    DDRD = 0xFF;
    PORTD = 0x00;

    TIMSK |= (1 << TOIE2);
    TCCR2 |= (1 << CS21);

    ADCSRA |= (1 << ADEN) | (1 << ADSC) | (1 << ADATE) | (1 << ADPS2) | (1 << ADPS1)

              | (1 << ADIE);
    ADMUX &= (~(1 << REFS1)) & (~(1 << REFS0));
    sei();
    while (1)
    {
        _delay_ms(50);
    }
}
ISR(ADC_vect)
{
    Display = ADC;
}
ISR(TIMER2_OVF_vect)
{
    PORTD = 0xFF;
    PORTC = (1 << current_indicator);
    switch (current_indicator)
    {
    case 0:
        PORTD = ~(SEG[display % 10000 / 1000]);
        break;
    case 1:
        PORTD = ~((SEG[display % 1000 / 100]));
        break;
    case 2:
        PORTD = ~(SEG[display % 100 / 10]);
        break;
    case 3:
        PORTD = ~(SEG[display % 10 / 1]);
        break;
    }
    if ((current_indicator++) > 2)
        current_indicator = 0;
}