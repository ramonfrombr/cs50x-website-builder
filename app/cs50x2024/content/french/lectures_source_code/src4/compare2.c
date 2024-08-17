// Affiche deux chaînes de caractères

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtient deux chaînes de caractères
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Affiche les chaînes de caractères
    printf("%s\n", s);
    printf("%s\n", t);
}