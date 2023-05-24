#include <avr/io.h>
#include <util/delay.h>

#include "i2c_eeprom.h"

void eeInit(void)
{
	// setup speed
    TWBR = (F_CPU/slaveF_SCL - 16)/(2 * /* TWI_Prescaler= 4^TWPS */1);
    

	/*
	If the TWI is operating in master mode, the TWBR value must be at least 10.
	If the TWBR value is less than 10, the bus master can generate incorrect signals
	on the SDA and SCL lines during the byte transfer.
	*/
    if(TWBR < 10)
        TWBR = 10;
    
	//Setting the prescaler in the status register of the Control Unit.
    TWSR &= (~((1<<TWPS1)|(1<<TWPS0)));
}

uint8_t eeWriteByte(uint16_t address,uint8_t data)
{
	// do, while we will not receive confirmation from the device
    do
    {
		/* (1<<TWINT) - reset to allow a new transmission
           (1<<TWSTA) - setup START
		   (1<<TWEN) - setup permission to work for TWI
		*/
		TWCR=(1<<TWINT)|(1<<TWSTA)|(1<<TWEN);
        while(!(TWCR & (1<<TWINT)));	// waiting for approval
		
	   // check I2C status
       if((TWSR & 0xF8) != TW_START)
            return false;

	   /* The constant part of the address 24LC64 - 1010 (see datasheet at 24XX64)
	      3 bits - variables (if suddenly we want to connect several identical chips
		  with the same factory addresses, they are useful, in another case, we set zeros)
		  then bit 0 - if you want to write to memory or 1 - if you read data from the memory of I2C EEPROM */
	   //TWDR = 0b1010‘000‘0
       TWDR = (slaveAddressConst<<4) + (slaveAddressVar<<1) + (WRITEFLAG);

	   // transfer the data contained in the data register TWDR
       TWCR=(1<<TWINT)|(1<<TWEN);

	   // waiting for the end of data transfer
       while(!(TWCR & (1<<TWINT)));
    
    }while((TWSR & 0xF8) != TW_MT_SLA_ACK);
        
    // write the most significant address bit in the data register
	// address 16 bit. so that first we transfer the highest digit, then the lower one
    TWDR=(address>>8);
	// send address
    TWCR=(1<<TWINT)|(1<<TWEN);

	// wait for end of transmit
    while(!(TWCR & (1<<TWINT)));

	// check I2C status
    if((TWSR & 0xF8) != TW_MT_DATA_ACK)
        return false;
	
	// send lower
    TWDR=(address);
    TWCR=(1<<TWINT)|(1<<TWEN);
    while(!(TWCR & (1<<TWINT)));

    if((TWSR & 0xF8) != TW_MT_DATA_ACK)
        return false;

    // send data
    TWDR=(data);
    TWCR=(1<<TWINT)|(1<<TWEN);
    while(!(TWCR & (1<<TWINT)));

    if((TWSR & 0xF8) != TW_MT_DATA_ACK)
        return false;
	
    // send STOP packet
    TWCR=(1<<TWINT)|(1<<TWEN)|(1<<TWSTO);
    
	// wait for accept STOP packet
    while(TWCR & (1<<TWSTO));

    return true;
}

uint8_t eeReadByte(uint16_t address)
{
    uint8_t data;
	// do similar tricks like in write function. establish conection with slave
    do
    {
        TWCR=(1<<TWINT)|(1<<TWSTA)|(1<<TWEN);
        while(!(TWCR & (1<<TWINT)));

        if((TWSR & 0xF8) != TW_START)
            return false;

        TWDR = (slaveAddressConst<<4) + (slaveAddressVar<<1) + WRITEFLAG;        
        TWCR=(1<<TWINT)|(1<<TWEN);

        while(!(TWCR & (1<<TWINT)));
    
    }while((TWSR & 0xF8) != TW_MT_SLA_ACK);
        
	// send address
    TWDR=(address>>8);
    TWCR=(1<<TWINT)|(1<<TWEN);
    while(!(TWCR & (1<<TWINT)));

    if((TWSR & 0xF8) != TW_MT_DATA_ACK)
        return false;

    TWDR=(address);
    TWCR=(1<<TWINT)|(1<<TWEN);
    while(!(TWCR & (1<<TWINT)));

    if((TWSR & 0xF8) != TW_MT_DATA_ACK)
        return false;

	
    // send REPEAT START packet
    TWCR=(1<<TWINT)|(1<<TWSTA)|(1<<TWEN);
    while(!(TWCR & (1<<TWINT)));

    if((TWSR & 0xF8) != TW_REP_START)
        return false;

	// send address with read flag
    TWDR = (slaveAddressConst<<4) + (slaveAddressVar<<1) + READFLAG;        

    TWCR=(1<<TWINT)|(1<<TWEN);
    while(!(TWCR & (1<<TWINT)));

    if((TWSR & 0xF8) != TW_MR_SLA_ACK)
        return false;


    TWCR=(1<<TWINT)|(1<<TWEN);

    while(!(TWCR & (1<<TWINT)));

	// check if data is valid
    if((TWSR & 0xF8) != TW_MR_DATA_NACK)
        return false;
	// get data from register
    data=TWDR;
	
	// send STOP packet
    TWCR=(1<<TWINT)|(1<<TWEN)|(1<<TWSTO);
    
    while(TWCR & (1<<TWSTO));

    return data;
}
