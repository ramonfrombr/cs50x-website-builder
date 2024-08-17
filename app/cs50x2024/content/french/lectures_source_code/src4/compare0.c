// Compare deux entiers

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Recevoir deux entiers
    int i = get_int("i: ");
    int j = get_int("j: ");

    // Comparer les entiers
    if (i == j)
    {
        printf("Identique\n");
    }
    else
    {
        printf("Différent\n");
    }
}