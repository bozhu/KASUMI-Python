/*---------------------------------------------------------
* Kasumi.h
*---------------------------------------------------------*/
#ifndef __KASUMI_H__
#define __KASUMI_H__

typedef unsigned char u8;
typedef unsigned short u16;
//typedef unsigned long u32;
typedef unsigned int u32;

void KeySchedule( u8 *key );
void Kasumi( u8 *data );

u16 KLi1[8], KLi2[8];
u16 KOi1[8], KOi2[8], KOi3[8];
u16 KIi1[8], KIi2[8], KIi3[8];

#include <stdio.h>

#endif //__KASUMI_H__
