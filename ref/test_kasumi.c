#include <stdio.h>
#include "kasumi.h"


int main(void)
{
    int i;

    u8 key[16] = {
        0x99, 0x00, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF,
        0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 
    };
    u8 text[8]  = {
        //0x12, 0x34, 0x56, 0x78, 0x90, 0xAB, 0xCD, 0xEF,
        0xFE, 0xDC, 0xBA, 0x09, 0x87, 0x65, 0x43, 0x21,
    };

    KeySchedule(key);
    /*
    for (i = 0; i < 8; i++)
        printf("%04x ", KLi1[i]);
    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%04x ", KLi2[i]);
    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%04x ", KOi1[i]);
    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%04x ", KOi2[i]);
    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%04x ", KOi3[i]);
    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%04x ", KIi1[i]);
    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%04x ", KIi2[i]);
    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%04x ", KIi3[i]);
    printf("\n");
    */

    Kasumi(text);

    //printf("\n");
    for (i = 0; i < 8; i++)
        printf("%02x ", text[i]);
    printf("\n");

    return 0;
}
