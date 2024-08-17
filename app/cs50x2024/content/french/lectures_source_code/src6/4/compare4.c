// Compare deux chaînes de caractères avec strcmp

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtenir deux chaînes de caractères
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Comparer les chaînes de caractères
    if (strcmp(s, t) == 0)
    {
        printf("Même\n");
    }
    else
    {
        printf("Différent\n");
    }
}