// Dépassement de capacité des entiers

#include <stdio.h>
#include <unistd.h>

int main(void)
{
    // Doublons itérativement i
    for (int i = 1; ; i *= 2)
    {
        printf("%i\n", i);
        sleep(1);
    }
}