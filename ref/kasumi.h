/*---------------------------------------------------------
* Kasumi.h
*---------------------------------------------------------*/
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned long u32;
void KeySchedule( u8 *key );
void Kasumi( u8 *data );
