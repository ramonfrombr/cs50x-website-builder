// Desbordamiento de enteros

#include <stdio.h>
#include <unistd.h>

int main(void)
{
    // Doblar i iterativamente
    for (int i = 1; ; i *= 2)
    {
        printf("%i\n", i);
        sleep(1);
    }
}