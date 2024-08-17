// Abstraction et domaine

#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("%i\n", i);
}

// Demander un entier positif à l'utilisateur
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