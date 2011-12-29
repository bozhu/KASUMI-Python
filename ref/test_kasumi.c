#include <stdio.h>
#include "kasumi.h"

int main(void)
{
    int i;

    u8 key[16] = {0};
    u8 text[8]  = {0};

    KeySchedule(key);
    Kasumi(text);

    for (i = 0; i < 8; i++)
        printf("%02x ", text[i]);
    printf("\n");

    return 0;
}
