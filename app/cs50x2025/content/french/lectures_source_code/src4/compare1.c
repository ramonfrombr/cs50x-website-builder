// Compare les adresses de deux chaînes de caractères

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtenir deux chaînes de caractères
    string s = get_string("s : ");
    string t = get_string("t : ");

    // Compare les adresses des chaînes de caractères
    if (s == t)
    {
        printf("Identique\n");
    }
    else
    {
        printf("Différent\n");
    }
}