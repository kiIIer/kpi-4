#define F_CPU 16000000UL

#include <avr/io.h>
#include "util/delay.h"
#include "i2c_eeprom.h"

int main(void)
{
	// delay for oscilloscope
	_delay_ms(4000); 

    uint8_t byte = 10;  // 0xA0
    uint16_t address = 25; //  0x19

    eeInit();	
    

	// check if byte writed successful
    if(eeWriteByte(address, byte))
    {    
		
        byte = 0; 
        
		// waite 15ms before read
        _delay_ms(15); 
        
        byte = eeReadByte(address); 
        
    }
}
