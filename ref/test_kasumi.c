#include <stdio.h>
#include "kasumi.h"


int main(void)
{
    int i;

    u8 key[16] = {0};
    u8 text[8]  = {0};

    KeySchedule(key);
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

    Kasumi(text);

    printf("\n");
    for (i = 0; i < 8; i++)
        printf("%02x ", text[i]);
    printf("\n");

    return 0;
}
