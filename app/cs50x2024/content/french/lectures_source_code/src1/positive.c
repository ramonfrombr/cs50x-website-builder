// Abstraction et portée

#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("%i\n", i);
}

// Invite l'utilisateur à saisir un entier positif
int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Entier positif : ");
    }
    while (n < 1);
    return n;
}