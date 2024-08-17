// Affiche les adresses de deux strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Récupération de deux strings
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Affiche les adresses des strings
    printf("%p\n", s);
    printf("%p\n", t);
}