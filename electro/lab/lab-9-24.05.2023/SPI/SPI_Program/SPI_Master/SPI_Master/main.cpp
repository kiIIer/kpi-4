/*
 * SPI_Master.cpp
 *
 * Created: 30.04.2018 4:23:45
 * Author : Юрій
 */ 

#define F_CPU 1000000
#include <avr/io.h>
#include <util/delay.h>

void SPI_MasterInit(void)
{
	DDRB = 0b00101111; // 3.1 Програмуємо виводи MOSI та SCK, SS, виводи 0 і 1 на вихід, а інші на вхід
	SPCR = (1<<SPE)|(1<<MSTR)|(1<<SPR0); // 3.2 Дозвіл роботи SPI, режим Master, встановлення швидкості передачі (fck/16)
}
char SPI_MasterTransmit_Receive(char cData)
{
	char received_Data;
	/* Початок передачі */
	
	SPDR = cData; // 6.1 Запис 8 біт даних для передачі в SPDR

	while(!(SPSR & (1<<SPIF))) // 6.2 
	; // 6.2 Чекаємо завершення передачі
	
	received_Data=SPDR; // 6.3 Читання прийнятих даних з регістра SPDR
	
	return received_Data;
}

int main(void)
{
	DDRD=0x00; // 1 Програмуємо порт D на вхід.
	PORTD=0x00; // 1 Відключаємо внутрішні підтягуючі резисторри, оскільки вони є на схемі.
	
	DDRC=0xff; // 2 Програмуємо виводи порта С на вихід.
	PORTC=0xff; // 2 Виводи порта С встановлюємо в 1.
	
	SPI_MasterInit(); // 3 Налаштування моуля SPI
	char data;
	
    while (1) // 4
    {
		data = PIND; // 5 Читання даних для передачі з порту D

		char r_Data = SPI_MasterTransmit_Receive(data); // 6 Прийом/передача даних

		PORTC = r_Data; // 7 Виведення 6 молодших біт прийнятих даних на PC0-PC5

		/* Виведення 2 старших біт прийнятих даних на PB6-PB7:*/
		char temp = PORTB; // 7
		temp &= 0b11111100; // 7
		temp |= ((r_Data>>6) & 0b00000011); // 7
		PORTB = temp; // 7
    } // 8
}

