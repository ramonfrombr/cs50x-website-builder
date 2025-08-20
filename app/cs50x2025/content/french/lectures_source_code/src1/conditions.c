// Conditions et opérateurs relationnels

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Demande à l'utilisateur x
    int x = get_int("x : ");

    // Demande à l'utilisateur y
    int y = get_int("y : ");

    // Compare x et y
    if (x < y)
    {
        printf("x est inférieur à y\n");
    }
    else if (x > y)
    {
        printf("x est supérieur à y\n");
    }
    else
    {
        printf("x est égal à y\n");
    }
}