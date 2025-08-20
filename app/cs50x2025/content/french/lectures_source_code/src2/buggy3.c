// Exemple buggé pour help50, debug50

#include <cs50.h>
#include <stdio.h>

int get_negative_int(void);

int main(void)
{
    int i = get_negative_int();
    printf("%i\n", i);
}

// Demande à l'utilisateur un entier positif
int get_negative_int(void)
{
    do
    {
        int n = get_int("Entier négatif : ");
    }
    while (n >= 0);
    return n;
}