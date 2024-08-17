// Compare deux chaînes à l'aide de strcmp et !

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtenir deux chaînes
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Comparer les chaînes
    if (strcmp(s, t) == 0)
    {
        printf("Identique\n");
    }
    else
    {
        printf("Différent\n");
    }
}